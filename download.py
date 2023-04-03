from __future__ import unicode_literals
from pathlib import Path
import json
import requests
import youtube_dl

class Downloader:
    def __init__(self):
        self._sources = json.load(Path("sources.json"))

    def download(self, entry, reddit):
        path = Path("data") / entry.sub
        type = entry.url_dest.split("/")[2]
        if type in self._sources["vid"]:
            dest = path / entry.title
            pass
        match entry.type:
            case "i.redd.it" | "i.imgur.com" | "redgifs.com":
                response = requests.get(entry.url)
            case "v.redd.it" | "gfycat.com":
                
            case "imgur.com":
                client_id = ""
                url = entry.url
                headers = {"Authorization": f"Client-ID {client_id}"}
                response = requests.get(url, headers = headers)

                album_data = response.json()["data"]
                img_links = [img["link"] for img in album_data["images"]]

                # dir = album_data["title"].replace(" ", "_")
                dir = entry.title
                p = Path(dir)
                p.mkdir(parents = True, exist_ok = True)
                count = 0
                for link in img_links:
                    fn = link.split("/")[-1]
                    fp = p / fn
                    response = requests.get(link)
                    with open(fp, "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded Imgur album {album_data['title']}: [{count}]/{len(img_links)}")
                    count += 1
            case "reddit.com":
                url = entry.url
                title = entry.title
                filename = f"{title}.html"
                with open(filename, "wb") as f:
                    response = reddit.session.get(url, headers = {"User-Agent": "Mozilla/5.0"})
                    f.write(response.content)
                    print(f"Downloaded {filename}")
            case _:

                print(f"Unkown domain for post '{entry.id}': {entry.domain}")

    def getGeneric(url, dest):
        try:
            with requests.get(url, stream = True) as r:
                r.raise_for_status()
                with open(dest, "wb") as f:
                    for chunk in r.iter_content(chunk_size = 1024 * 1024 * 1): # 1 MB
                        f.write(chunk)
            return True
        except Exception as e:
            print(f"Could not download {url}")
            raise e
    def getYT(url, dest):
        try:
            ydl_opts = {
                        "format": "bestaudio/best",
                        "quiet": True,
                        "outtmpl": f"{dest}.%(ext)s"
                    }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([entry.url])
        except Exception as e:
            print(f"Could not download {url}")
