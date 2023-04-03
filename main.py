import praw
import json

class Account:
    user_agent = "Geddit 1.0 by /u/aeluro1"

    def __init__(self):
        with open("user.json") as f:
            self._info = json.load(f)
        self._saved_posts = ""
        _reddit = praw.Reddit(user_agent = Account.user_agent)

    def getSavedPosts(self):
        _saved_posts = [item in r.user.me().saved(limit = None) if isinstance(item, praw.Models.Submission)]

def main():


    with open("list.txt", "w") as f:
        for item in r.user.me().saved(limit=None):
            print(item.id)
            if isinstance(item, praw.Models.Submission): # Ignore comments
                f.write()
                if item.is_self:
                    f.write(item.selftext + '\n')
                else:
                    f.write(item.url)
            sub = r.submission(id = item.id)

if __name__ == "__main__":
    main()