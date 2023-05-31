import json
import csv
import argparse
from pathlib import Path

import requests
import praw

from download import Downloader


class Posts:
    post_path = Path("data/posts.json")
    fail_path = Path("data/failed.json")
    csv_path = Path("saved_posts.csv")

    downloader = Downloader()

    def __init__(self, account: "Account", debug: bool = False, csv: bool = False, verbose: bool = False):
        self._posts = self.load_JSON(Posts.post_path)
        self._failed  = {}

        self._all_posts = []
        
        Posts.post_path.parent.mkdir(parents = True, exist_ok = True)

        self._account = account

        self._added_count = 0
        self._failed_count = 0
        self._skipped = 0
        self._counter = 0

        self._debug = debug
        self._csv = csv
        self._verbose = verbose
        Posts.downloader.verbose = verbose

        self.msg("Initialized!")

    def get_posts(self):
        reddit = self._account.reddit
        
        if self._csv:
            self._all_posts = reddit.info(fullnames = self.load_CSV(Posts.csv_path))
        else:
            self._all_posts = reddit.user.me().saved(limit = None)

    def download_all(self):
        for post in self._all_posts:
            self.download_post(post)
        
    def download_post(self, post: praw.models.Submission):
        # Skip all comment instances
        if not isinstance(post, praw.models.Submission):
            return
        
        if post.id in self._posts:
            self._skipped += 1
            self.msg(f"Skipped post {post.id} from r/{self._posts[post.id]['sub']} - already in database")
            return
        
        entry = self.process_post(post)
        self.download_entry(entry, post.id)

    def process_post(self, praw_post: praw.models.Submission) -> dict:
        if not isinstance(praw_post, praw.models.Submission):
            raise ValueError("Argument must be PRAW submission object")
        
        post = self.get_post(praw_post.id)
        # post = self.postToDict(praw_post)
        post = self.fix_crosspost(post)
        entry = self.generate_entry(post)
        if entry["source"] == "" or entry["url"] == "" or entry["data"] == "[removed]" or entry["data"] == []:
            ps = self.get_praw_post(post["id"])
            if ps is not {}:
                entry = self.generate_entry(ps)
        
        return entry

    def generate_entry(self, post: dict) -> dict:
        title = post.get("title", "").encode("ascii", "ignore").decode()
        author = str(post.get("author", "")) if post.get("author", "") is not None else "[deleted]"
        url = post.get("url_overridden_by_dest", post.get("url", ""))

        try:
            url_preview = post["preview"]["images"][0]["source"]["url"]
        except Exception:
            if "i.redd.it" in url:
                url_preview = url.replace("i.redd.it", "preview.redd.it")
            else:
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
            entry["data"] = self.process_gallery(url)

        # Image links can be obtained by simply appending extension to url
        if "imgur" in url and "/a/" not in url and Path(url).suffix == "":
            entry["url"] += ".png"

        return entry

    def download_entry(self, entry: dict, id: str):
        try:
            if not self._debug:
                Posts.downloader.download(entry, id)
            self._added_count += 1
            self._posts[id] = entry
            self.msg(f"Added post {id} from r/{entry['sub']}")
        except Exception as e:
            self._failed_count += 1
            entry["error"] = str(e)
            self._failed[id] = entry
            self.msg(f"Failed to add post {id} from r/{entry['sub']}: {str(e)}")

        self._counter += 1
        if self._counter == 50:
            self.save_all(temp = True)
            self._counter = 0

    def get_post(self, id: str) -> dict:
        post = self.get_pushshift_post(id)
        if post != {}:
            return post
        return self.get_praw_post(id)

    def get_pushshift_post(self, id: str) -> dict:
        if self._verbose: print(f"[Calling pushshift for post {id}]")

        ps_api = "https://api.pushshift.io/reddit/search/submission"
        try:
            response = requests.get(ps_api, headers = Downloader.headers, params = {"ids": id}, timeout = 30)
            response.raise_for_status()
            post = response.json()["data"][0]
            return post
        except Exception:
            return {}

    def get_praw_post(self, id: str) -> dict:
        if self._verbose: print(f"[Calling PRAW for post {id}]")

        try:
            praw_post = self._account.reddit.submission(id = id)
            if hasattr(praw_post, "title") or True: # Verifies and loads PRAW object to deal with rare cases where submission object errors
                post = vars(praw_post)
            return post
        except Exception:
            return {}

    def fix_crosspost(self, post: dict) -> dict:
        xposts = post.get("crosspost_parent_list", None)
        if xposts is not None and len(xposts) > 0:
            post = self.get_post(xposts[-1]["id"])
        return post

    def process_gallery(self, link: str) -> list[str]:
        if self._verbose: print(f"Processing gallery at {link}")

        id = link.strip("/").split("/")[-1]
        urls = []
        
        if "reddit.com/gallery/" in link:
            post = self.get_post(id)

            if post.get("gallery_data", None) is None:
                return urls

            # Get links to each image in Reddit gallery
            # Try block to account for possibility of some posts media data not containing "p", "u", etc. elements
            try:
                ord = [i["media_id"] for i in post["gallery_data"]["items"]]
                for key in ord:
                    img = post["media_metadata"][key]
                    if len(img["p"]) > 0:
                        url = img["p"][-1]["u"]
                    else:
                        url = img["s"]["u"]
                    url = url.split("?")[0].replace("preview", "i")
                    urls.append(url)
            except Exception as e:
                if self._verbose: print(e)
                return urls
        
        elif "imgur.com/a/" in link:
            headers = dict(Downloader.headers)
            headers.update({
                "Authorization": f"Client-ID {self._account.imgur_key[0]}"
            })

            try:
                response = requests.get(f"https://api.imgur.com/3/album/{id}/images", headers = headers, timeout = 30)
                response.raise_for_status()
                urls = [item["link"] for item in response.json()["data"]]

                if int(response.headers["x-ratelimit-clientremaining"]) < 1000:
                    self._account.imgur_key.pop(0)
            except Exception as e:
                if self._verbose: print(e)
            
        return urls
    
    def save_all(self, temp: bool = False):
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

    def load_JSON(self, path: Path) -> list[praw.models.Submission]:
        if not path.is_file():
            return {}
        
        with open(path) as f:
            posts = json.load(f)

        path_temp = Path(str(path) + "_temp")

        if path_temp.is_file():
            with open(path_temp) as f:
                posts.update(json.load(f))

        return posts
    
    def load_CSV(self, path: Path) -> list[str]:
        if not path.is_file():
            return []
        
        with open(path, newline = "", encoding = "utf-8") as f:
            reader = csv.reader(f)
            ids = [row[0] for row in reader]
            del ids[0]

        names = [id if id.startswith("t3_") else f"t3_{id}" for id in ids]
        
        return names
            
    def msg(self, msg):
        print(f"[T: {len(self._posts)}][A: {self._added_count}][F: {self._failed_count}][S: {self._skipped}] {msg}")


class Account:
    user_agent = "Geddit Saved Posts Backup Utiity (by /u/aeluro1)"

    def __init__(self):
        with open("user.json") as f:
            data = json.load(f)

        self._info = data["reddit"]
        self._imgur_key = data["imgur"]["client_id"]

        self._reddit = praw.Reddit(
            user_agent = Account.user_agent,
            client_id = self._info["client_id"],
            client_secret = self._info["client_secret"],
            username = self._info["username"],
            password = self._info["password"]
        )
        
        if not isinstance(self._imgur_key, list):
            raise ValueError("Update user.json Imgur key format")

    @property
    def reddit(self):
        return self._reddit
    
    @property
    def imgur_key(self):
        return self._imgur_key


def main(args):
    account = Account()
    posts = Posts(account, args.debug, args.csv, args.verbose)
    posts.get_posts()
    posts.download_all()
    posts.save_all(temp = False)


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