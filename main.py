import praw
import json
from pathlib import Path

from utils import toAscii

class Posts:
    post_path = Path("./data/posts.json")

    def __init__(self):
        if (Posts.post_path.is_file()):
            with open(Posts.post_path) as f:
                self._posts = json.load(f)
        else:
            self._posts = {}

        self._newCount = 0

    def getNewPosts(self, reddit):
        for item in reddit.user.me().saved(limit = None):
            if isinstance(item, praw.models.Submission):
                self.addPost(item)

    def addPost(self, post):
        post.title = toAscii(post.title)
        
        entry = {
            "sub": post.subreddit.display_name,
            "title": post.title,
            "author": (post.author.name if post.author is not None else None),
            "date": post.created_utc,
            "type": post.domain,
            "url": post.url,
            "url_dest": (post.url_overridden_by_dest if hasattr(post, "url_overridden_by_dest") else "")
        }

        if post.id in self._posts:
            print(f"[Total: {len(self._posts)}][New: {self._newCount}] Skipped post '{entry['title']}' from '{entry['sub']}'. Already in database.")
            return

        self._posts[post.id] = entry
        self._newCount += 1

        print(f"[Total: {len(self._posts)}][New: {self._newCount}] Added post '{entry['title']}' from '{entry['sub']}'")

    def save(self):
        print("Saving posts to JSON...")
        with open(Posts.post_path, "w") as f:
            json.dump(self._posts, f, indent = 4)


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