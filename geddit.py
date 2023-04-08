import praw
import json
import csv
import argparse
from pathlib import Path

import requests

from download import Downloader


class Posts:
    post_path = Path("data/posts.json")
    fail_path = Path("data/failed.json")
    csv_path = Path("saved_posts.csv")

    downloader = Downloader()

    def __init__(self, account: "Account", debug: bool, csv: bool, verbose: bool):
        self._posts = self.loadJSON(Posts.post_path)
        self._failed  = {}

        self._allPosts = []
        
        Posts.post_path.parent.mkdir(parents = True, exist_ok = True)

        self._account = account

        self._addedCount = 0
        self._failedCount = 0
        self._skipped = 0
        self._counter = 0

        self._debug = debug
        self._csv = csv
        self._verbose = verbose
        Posts.downloader.verbose = verbose

        self.msg("Initialized!")

    def getPosts(self):
        reddit = self._account.reddit
        
        if self._csv:
            self._allPosts = reddit.info(fullnames = self.loadCSV(Posts.csv_path))
        else:
            self._allPosts = reddit.user.me().saved(limit = None)

    def downloadAll(self):
        for post in self._allPosts:
            self.downloadPost(post)
        
    def downloadPost(self, post):
        if not isinstance(post, praw.models.Submission): # Comment
            return
        
        if post.id in self._posts:
            self._skipped += 1
            self.msg(f"Skipped post {post.id} from r/{self._posts[post.id]['sub']} - already in database")
            return
        
        entry = self.processPost(post)
        self.downloadEntry(entry, post.id)

    def processPost(self, post: praw.models.Submission) -> dict:
        if not isinstance(post, praw.models.Submission):
            return None
        
        post = self.fixCrosspost(post)
        entry = self.generateEntry(post)
        if entry["source"] == "" or entry["url"] == "" or entry["data"] == "[removed]" or entry["data"] == []:
            ps = self.getPushshiftInfo(post.id)
            entry = self.generateEntry(ps)
        
        return entry

    def generateEntry(self, post: dict | praw.models.Submission) -> dict:
        if isinstance(post, praw.models.Submission): # Necessary to load lazy objects
            title = post.title if hasattr(post, "title") else ""
            post = vars(post)
        else: # If post is already dictionary, i.e. from pushshift
            title = post.get("title", "")
        title = title.encode("ascii", "ignore").decode()
        author = str(post.get("author", "")) if post.get("author", "") is not None else "[deleted]"
        url = post.get("url_overridden_by_dest", post.get("url", ""))

        try:
            url_preview = post["preview"]["images"][0]["source"]["url"]
        except:
            url_preview = ""

        entry = {
            "sub": str(post.get("subreddit", "")),
            "title": title,
            "author": author,
            "date": post.get("created_utc", 0.0),
            "source": post.get("domain", ""),
            "url": url,
            "url_preview": url_preview,
            "data": "",
        }
        
        if post.get("is_self", False):
            entry["data"] = post.get("selftext", "")
        elif "reddit.com/gallery/" in url or "imgur.com/a/" in url:
            entry["data"] = self.processGallery(url)

        return entry

    def getPushshiftInfo(self, id: str) -> dict:
        print(f"[Calling pushshift for post {id}]")
        ps_api = "https://api.pushshift.io/reddit/search/submission"
        try:
            response = requests.get(ps_api, headers = Downloader.headers, params = {"ids": id}, timeout = 30)
            response.raise_for_status()
            data = response.json()["data"][0]
            return data
        except:
            return {}

    def downloadEntry(self, entry: dict, id: str):
        try:
            if not self._debug:
                Posts.downloader.download(entry, id)
            self._addedCount += 1
            self._posts[id] = entry
            self.msg(f"Added post {id} from r/{entry['sub']}")
        except Exception as e:
            self._failedCount += 1
            entry["error"] = str(e)
            self._failed[id] = entry
            self.msg(f"Failed to add post {id} from r/{entry['sub']}: {str(e)}")

        self._counter += 1
        if self._counter == 50:
            self.saveAll(temp = True)
            self._counter = 0

    def fixCrosspost(self, post: praw.models.Submission) -> praw.models.Submission:
        xposts = post.crosspost_parent_list if hasattr(post, "crosspost_parent_list") else None
        if xposts is not None and len(xposts) > 0:
            post = self._account.reddit.submission(id = xposts[-1]["id"])
        return post

    def processGallery(self, link: str) -> list[str]:
        if self._verbose:
            print(f"Processing gallery at {link}")

        # Append Reddit gallery data to 'entry' so that it is not necessary to use PRAW again when downloading
        id = link.strip("/").split("/")[-1]
        urls = []
        
        if "reddit.com/gallery/" in link:
            post = self._account.reddit.submission(id = id)

            if not hasattr(post, "gallery_data") or post.gallery_data is None:
                try:
                    ps = self.getPushshiftInfo(id)
                    gallery_data = ps["gallery_data"]
                    media_metadata = ps["media_metadata"]
                    if gallery_data is None:
                        raise ValueError("Unable to extract album data via pushshift and praw")
                except:
                    return urls
            else:
                gallery_data = post.gallery_data
                media_metadata = post.media_metadata

            ord = [i["media_id"] for i in gallery_data["items"]]
            
            # Get links to each image in Reddit gallery
            for key in ord:
                img = media_metadata[key]
                if len(img["p"]) > 0:
                    url = img["p"][-1]["u"]
                else:
                    url = img["s"]["u"]
                url = url.split("?")[0].replace("preview", "i")
                urls.append(url)
        
        elif "imgur.com/a/" in link:
            headers = dict(Downloader.headers)
            headers.update({
                "Authorization": f"Client-ID {self._account.imgurKey[0]}"
            })

            try:
                response = requests.get(f"https://api.imgur.com/3/album/{id}/images", headers = headers, timeout = 30)
                response.raise_for_status()
                urls = [item["link"] for item in response.json()["data"]]

                if int(response.headers["x-ratelimit-clientremaining"]) < 1000:
                    self._account.imgurKey.pop(0)
            except Exception as e:
                if self._verbose:
                    print(e)
            
        return urls
    
    def saveAll(self, temp: bool = False):
        files = [(self._posts, Posts.post_path), (self._failed, Posts.fail_path)]

        self.msg(f"Saving items to JSON...")
        
        for (data, path) in files:
            self.save(data, path, temp = temp)

    def save(self, data: dict, path: Path, temp: bool = False):
        if self._debug:
            path = Path(str(path) + "_debug")

        path_temp = Path(str(path) + "_temp")

        if temp:
            path = path_temp
        else:
            if path_temp.is_file():
                path_temp.unlink()
        
        with open(path, "w") as f:
            json.dump(data, f, indent = 4)

    def loadJSON(self, path: Path) -> list[praw.models.Submission]:
        if path.is_file():
            with open(path) as f:
                posts = json.load(f)
        else:
            posts = {}

        path_temp = Path(str(path) + "_temp")

        if (path_temp).is_file():
            with open(path_temp) as f:
                posts.update(json.load(f))

        return posts
    
    def loadCSV(self, path: Path) -> list[str]:
        if not path.is_file():
            return []
        with open(path, newline = "", encoding = "utf-8") as f:
            reader = csv.reader(f)
            ids = [row[0] for row in reader]
            del ids[0]
        names = [id if id.startswith("t3_") else f"t3_{id}" for id in ids]
        return names
            
    def msg(self, msg):
        print(f"[T: {len(self._posts)}][A: {self._addedCount}][F: {self._failedCount}][S: {self._skipped}] {msg}")


class Account:
    user_agent = "Geddit 1.0 by /u/aeluro1"

    def __init__(self):
        with open("user.json") as f:
            data = json.load(f)
        self._info = data["reddit"]
        self._imgurKey = data["imgur"]["client"]

        self._reddit = praw.Reddit(
            user_agent = Account.user_agent,
            client_id = self._info["client"],
            client_secret = self._info["secret"],
            username = self._info["user"],
            password = self._info["pass"]
        )
        if not isinstance(self._imgurKey, list):
            raise ValueError("Update user.json Imgur key format")

    @property
    def reddit(self):
        return self._reddit
    
    @property
    def imgurKey(self):
        return self._imgurKey


def main(args):
    account = Account()
    posts = Posts(account, args.debug, args.csv, args.verbose)
    posts.getPosts()
    posts.downloadAll()
    posts.saveAll(temp = False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Geddit")
    parser.add_argument(
        "--debug", "-d",
        action = "store_true",
        help = "to activate debug mode, where no files are downloaded",
    )
    parser.add_argument(
        "--csv",
        action = "store_true",
        help = "to process saved posts .csv file",
    )
    parser.add_argument(
        "--verbose", "-v",
        action = "store_true",
        help = "to print all log statements",
    )
    args = parser.parse_args()

    main(args)