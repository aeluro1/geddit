import requests

def true_link(url):
    try:
        response = requests.head(url, allow_redirects = True, timeout = 10)
        response.raise_for_status()
        return response.url.split("?")[0]
    except Exception:
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