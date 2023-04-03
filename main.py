import praw
import json
import pprint

import link_parser as p

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

        self._saved_posts = {}

        for item in self._reddit.user.me().saved(limit = None):
            if isinstance(item, praw.models.Submission):
                self._saved_posts[item.id] = item
                # type = {
                #     None: None
                # }
                # entry = {
                #     "title": item.title,
                #     "id": item.id,
                #     "author": item.author, # Redditor object
                #     "url": item.url,
                # created_utc, author_fullname, domain
                #     "sub": None,
                #     "type": type
                # }

    @property
    def reddit(self):
        return self._reddit
    
    @property
    def saved_posts(self):
        return self._saved_posts

class Node:
    def __init__(self, submission):
        if submission is None:
            return None
        self.name_

def main():
    test = Account()
    
    for item in test._reddit.user.me().saved(limit = None):
        print(item)
        pprint.pprint(vars(item))



    # with open("list.txt", "w") as f:
    #     for item in r.user.me().saved(limit=None):
    #         print(item.id)
    #         if isinstance(item, praw.Models.Submission): # Ignore comments
    #             f.write()
    #             if item.is_self:
    #                 f.write(item.selftext + '\n')
    #             else:
    #                 f.write(item.url)
    #         sub = r.submission(id = item.id)

if __name__ == "__main__":
    main()