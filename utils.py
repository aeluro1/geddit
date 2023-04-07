import requests
from urllib.parse import urlsplit, urlunsplit

def trueLink(url):
    try:
        response = requests.head(url, allow_redirects= True, timeout = 5)
        return response.url.split("?")[0]
    except:
        return url

class BlankLogger:
    def debug(self, msg):
        pass
    def error(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        pass