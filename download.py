import praw
import json

class Account:
    def __init__(self):
        with open("user.json") as f:
            self._info = json.load(f)
        self._saved_posts = ""

def main():

    user_agent = "Geddit 1.0 by /u/aeluro1"

    r = praw.Reddit(
        user_agent = user_agent
    )

    r.login()

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