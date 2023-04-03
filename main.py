import praw
import json
from pathlib import Path

from utils import toAscii
from download import Downloader

class Posts:
    post_path = Path("data/posts.json")
    fail_path = Path("data/failed.json")
    downloader = Downloader()

    def __init__(self):
        if (Posts.post_path.is_file()):
            with open(Posts.post_path) as f:
                self._posts = json.load(f)
        else:
            self._posts = {}

        self._addedCount = 0
        self._failedCount = 0
        self._failed = {}
        self._counter = 0

    def getNewPosts(self, reddit):
        for item in reddit.user.me().saved(limit = None):
            if isinstance(item, praw.models.Submission):

                if item.removed_by_category is not None:
                    continue

                xposts = item.__dict__.get("crosspost_parent_list", None)
                if xposts is not None and len(xposts) > 0:
                    item = reddit.submission(id = xposts[-1]["id"])

                self.addPost(item)

    def addPost(self, post):
        post.title = toAscii(post.title)

        entry = {
            "sub": post.subreddit.display_name,
            "title": post.title,
            "author": (post.author.name if post.author is not None else None),
            "date": post.created_utc,
            "source": post.domain,
            "url": (post.url_overridden_by_dest if hasattr(post, "url_overridden_by_dest") else post.url),
            "data": "",
        }

        if "reddit" in entry["source"] and "/gallery/" in entry["url"]:
            urls = []
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
            entry["data"] = urls

        if post.id in self._posts:
            self.msg(f"Skipped post {post.id} from r/{entry['sub']}. Already in database.")
            return
        
        try:
            Posts.downloader.download(entry)
            self._addedCount += 1
            self.msg(f"Added post {post.id} from r/{entry['sub']}")
            self._posts[post.id] = entry
        except Exception as e:
            self.msg(f"Failed to add post {post.id} ({entry['url']}) from r/{entry['sub']}: {str(e)}")
            self._failedCount += 1
            entry["errpr"] = str(e)
            self._failed[post.id] = entry

        self._counter += 1
        if self._counter == 100:
            self.save()
            self._counter = 0

    def save(self):
        self.msg("Saving posts to JSON...")

        Posts.post_path.parent.mkdir(parents = True, exist_ok = True)

        with open(Posts.post_path, "w") as f:
            json.dump(self._posts, f, indent = 4)

        with open(Posts.fail_path, "w") as f:
            json.dump(self._failed, f, indent = 4)

    def msg(self, msg):
        print(f"[Total: {len(self._posts)}][Added: {self._addedCount}][Failed: {self._failedCount}] {msg}")


class Account:
    user_agent = "Geddit 1.0 by /u/aeluro1"

    def __init__(self):
        with open("user.json") as f:
            self._info = json.load(f)["reddit"]

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

def main():
    r = Account()
    p = Posts()
    p.getNewPosts(r.reddit)
    p.save()

if __name__ == "__main__":
    main()