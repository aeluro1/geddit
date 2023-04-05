import requests

def trueLink(url):
    response = requests.get(url, timeout = 5, allow_redirects= True)
    return response.url

def getPreview(post, entry): # only works for single-image posts, not albums. need to check if it exists for text posts and comments as well
    if hasattr(post, 'preview["images"][0]["source"]["url"]'):
        entry["data"] = post.preview["images"][0]["source"]["url"]

class BlankLogger:
    def debug(self, msg):
        pass
    def error(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        pass