import praw
import json
import csv
import argparse
from pathlib import Path

import requests

from download import Downloader
from utils import trueLink


class Posts:
    post_path = Path("data/posts.json")
    fail_path = Path("data/failed.json")
    csv_path = Path("saved_posts.csv")

    downloader = Downloader()

    def __init__(self, account):
        self._posts, self._failed = self.load()
        self._allEntries = {}
        
        Posts.post_path.parent.mkdir(parents = True, exist_ok = True)

        self._account = account

        self._addedCount = 0
        self._failedCount = 0
        self._skipped = 0
        self._counter = 0

    def getItems(self):
        reddit = self._account.reddit
        
        csvItems = reddit.info(fullnames = self.loadCSV())
        liveItems = reddit.user.me().saved(limit = None)
        sources = [csvItems, liveItems]

        allItems = set()
        for source in sources:
            allItems.update([item for item in source])

        for item in allItems:
            self._allEntries[item.id] = self.processItem(item)

    def downloadAll(self):
        for (key, val) in enumerate(self._allEntries):
            self.downloadEntry(val, key)

    def processItem(self, item):
        print(item)
        if isinstance(item, praw.models.Submission):
            item = self.fixCrosspost(item)
            entry = self.generateEntry(item)
            entry["data"] = self.processGallery(entry["url"])
            
            return entry
        else:
            # Handle comments here
            pass

    def generateEntry(self, item):
        title = item.title.encode("ascii", "ignore").decode()
        author = item.author.name if item.author is not None else None
        url = item.url_overridden_by_dest if hasattr(item, "url_overridden_by_dest") else item.url
        try:
            url_preview = item.preview["items"][0]["source"]["url"]
        except:
            url_preview = None

        entry = {
            "sub": item.subreddit.display_name,
            "title": title,
            "author": author,
            "date": item.created_utc,
            "source": item.domain,
            "url": trueLink(url),
            "url_preview": url_preview,
            "data": None,
        }
        return entry

    def downloadEntry(self, entry, id):
        if id in self._posts:
            self._skipped += 1
            self.msg(f"Skipped post {id} from r/{entry['sub']} - already in database")
            return

        try:
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
            self.save(temp = True)
            self._counter = 0

    def fixCrosspost(self, item):
        xposts = item.__dict__.get("crosspost_parent_list", None)
        if xposts is not None and len(xposts) > 0:
            item = self._account.reddit.submission(id = xposts[-1]["id"])
        return item

    def processGallery(self, link):
        # Append Reddit gallery data to 'entry' so that it is not necessary to use PRAW again when downloading
        id = link.strip("/").split("/")[-1]
        urls = []
        
        if "reddit.com/gallery/" in link:
            post = self._account.reddit.submission(id)

            ord = [i["media_id"] for i in post.gallery_data["items"]]
            
            # Get links to each image in Reddit gallery
            for key in ord:
                img = post.media_metadata[key]
                if len(img["p"]) > 0:
                    url = img["p"][-1]["u"]
                else:
                    url = img["s"]["u"]
                url = url.split("?")[0].replace("preview", "i")
                urls.append(url)
        
        elif "imgur.com/a/" in link:
            headers = {
                "Authorization": f"Client-ID {self._account.imgurKey}"
            }
            response = requests.get(f"https://api.imgur.com/3/album/{id}/images", headers = headers, timeout = 5)
            urls = [item["link"] for item in response.json()["data"]]
            
        return urls

    def save(self, temp = False):
        self.msg("Saving posts to JSON...")

        post_path = Posts.post_path
        fail_path = Posts.fail_path
        post_path_temp = Path(str(Posts.post_path) + "_temp")
        fail_path_temp = Path(str(Posts.fail_path) + "_temp")

        if temp:
            post_path = post_path_temp
            fail_path = fail_path_temp
        else:
            if post_path_temp.is_file():
                post_path_temp.unlink()
            if fail_path_temp.is_file():
                fail_path_temp.unlink()
        
        with open(post_path, "w") as f:
            json.dump(self._posts, f, indent = 4)

        with open(fail_path, "w") as f:
            json.dump(self._failed, f, indent = 4)

    def load(self):
        if Posts.post_path.is_file():
            with open(Posts.post_path) as f:
                good_posts = json.load(f)
        else:
            good_posts = {}

        if Posts.fail_path.is_file():
            with open(Posts.fail_path) as f:
                bad_posts = json.load(f)
        else:
            bad_posts = {}

        post_path_temp = Path(str(Posts.post_path) + "_temp")
        fail_path_temp = Path(str(Posts.fail_path) + "_temp")

        if (post_path_temp).is_file():
            with open(post_path_temp) as f:
                good_posts.update(json.load(f))

        if (fail_path_temp).is_file():
            with open(fail_path_temp) as f:
                bad_posts.update(json.load(f))

        return (good_posts, bad_posts)
    
    def loadCSV(self):
        if not self.csv_path.is_file():
            return []
        with open(self.csv_path, newline = "", encoding = "utf-8") as f:
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

    @property
    def reddit(self):
        return self._reddit
    
    @property
    def imgurKey(self):
        return self._imgurKey

def main(args):
    account = Account()
    posts = Posts(account)
    posts.getItems()
    posts.save(temp = False)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Geddit")
    parser.add_argument(
        "--debug", "-d",
        action = "store_true",
        dest = "debug",
        help = "to activate debug mode, where no files are downloaded",
    )
    args = parser.parse_args()

    main(args)