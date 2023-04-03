import praw
import json
import pprint

class Account:
    user_agent = "Geddit 1.0 by /u/aeluro1"

    def __init__(self):
        with open("user.json") as f:
            self._info = json.load(f)

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
    acc = Account()
    
        # print("Post ID: ")
        # id = input()

    item = acc.reddit.submission(url = "https://www.reddit.com/r/gifs/comments/127dtvi/my_newest_creation_the_jadelux_philosophers/")
    
    print(item.title)
    # print(vars(item))
    pprint.pprint(vars(item))

if __name__ == "__main__":
    main()