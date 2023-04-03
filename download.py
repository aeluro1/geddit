from __future__ import unicode_literals
from pathlib import Path
from mimetypes import guess_extension
import json
import re

import requests
import youtube_dl

from utils import unzip

class Downloader:

    def __init__(self):
        with open("sources.json") as f:
            self._sources = json.load(f)

    def download(self, entry):
        dest = Path("data") / entry["sub"]
        url = entry["url"]
        source = entry["source"]
        title = re.sub(r"[\\/*?:.\"<>|]", "", entry["title"])

        # Create subreddit folder if non-existent, then set 'dest' to include post file/folder
        dest.mkdir(parents = True, exist_ok = True)
        dest = dest / title

        if source in self._sources["vid"]:
            self.getVid(url, dest)
        elif source in self._sources["img"]:
            if "imgur" in source and "/a/" in url:
                url += "/zip"
                self.getAlbum([url], dest)
                # headers = {}#"Authorization": f"Client-ID {client_id}"}
                # response = requests.get(url, headers = headers)

                # album_data = response.json()["data"]
                # urls = [img["link"] for img in album_data["images"]]

                # self.getAlbum(urls, dest)
            elif "reddit" in source and "/gallery/" in url:
                self.getAlbum(entry["data"], dest)
            elif ".gifv" in url:
                self.getVid(url, dest)
            else:
                self.getGeneric(url, dest)
        # if source.startswith("self."):
        #     url = entry.url
        #     title = entry.title
        #     filename = f"{title}.html"
        #     with open(filename, "wb") as f:
        #         response = reddit.session.get(url, headers = {"User-Agent": "Mozilla/5.0"})
        #         f.write(response.content)
        #         print(f"Downloaded {filename}")
        else:
            # head = requests.head(url)["content-type"]
            raise Exception(f"Unkown domain for post '{title}': {source}")

    def getGeneric(self, url, dest):
        with requests.get(url, stream = True) as r:
            r.raise_for_status()
            ext = guess_extension(r.headers["content-type"].split(";")[0].strip())
            dest = Path(str(dest) + ext)
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size = 1024 * 1024 * 1): # 1 MB
                    f.write(chunk)
        
    def getVid(self, url, dest):
        ydl_opts = {
                    # "quiet": True,
                    "no_warnings": True,
                    "outtmpl": f"{dest}.%(ext)s",
                    "postprocessors": [{
                        "key": "FFmpegVideoConvertor",
                        "preferedformat": "mp4"
                    }]
                }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def getAlbum(self, urls, dest):
        dest.mkdir(parents = True, exist_ok = True)
        count = 0

        for url in urls:
            self.getGeneric(url, dest / str(count))
            print(f"[Downloading album: {count}/{len(urls)}]")
            count += 1

        if "imgur" in urls[0]:
            unzip(dest / "0.zip", dest.parent)