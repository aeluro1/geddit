from bs4 import BeautifulSoup
import requests
from time import sleep

def getPushshiftPost(id: str) -> dict:
    ps_api = "https://api.pushshift.io/reddit/search/submission"
    try:
        response = requests.get(ps_api, params = {"ids": id}, timeout = 30)
        response.raise_for_status()
        post = response.json()["data"]
        if not post == []:
            return post[0]
    except:
        pass
    return {}

def getWayback(url):
    urls = []

    wb_api = "https://web.archive.org/cdx/search/cdx"
    wb_src = "https://web.archive.org/web"

    params = {
        "url": url,
        "output": "json",
        "gzip": False,
        "fl": "timestamp,statuscode",
        "collapse": "digest",
        "matchType": "prefix"
    }
    response = requests.get(wb_api, params = params, timeout = 30)
    if response.status_code == 429:
        print("[Wayback machine is overloaded - waiting 1 minute]")
        sleep(61)
        response = requests.get(wb_api, params = params, timeout = 30)
    response.raise_for_status()

    captures = response.json()
    if len(captures) != 0:
        stamps = captures[1:]
        stamps = [stamp for stamp in stamps if stamp[1].isdigit()]
        stamps = sorted(stamps, key = lambda x: int(x[1]))
        urls = [wb_src + f"/{stamp[0]}/{url}" for stamp in stamps]
    
    return urls[:3]



id = ""
url = getPushshiftPost(id)["url"]
print(url)
urls = getWayback(url)
for u in urls:
    response = requests.get(u)
    soup = BeautifulSoup(response.content, "html.parser")
    i = soup.find_all("a", class_ = "styled-outbound-link")
    if len(i) != 0:
        print(i[0]["href"])
        break