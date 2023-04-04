from __future__ import unicode_literals
from pathlib import Path
from mimetypes import guess_extension
import json
import re

import requests
from yt_dlp import YoutubeDL
from fake_useragent import UserAgent

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
                self.getImgurAlbum(url, dest)
            elif "reddit" in source and "/gallery/" in url:
                self.getAlbum(entry["data"], dest)
            elif ".gifv" in url:
                self.getVid(url, dest)
            else:
                self.getGeneric(url, dest)
        elif source.startswith("self."):
            self.getGeneric(url, dest)
        else:
            mediaType = requests.head(url).headers["content-type"]
            if "image" in mediaType.lower():
                self.getGeneric(url, dest)
            elif "video" in mediaType.lower():
                self.getVid(url, dest)
            else:
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
                    "quiet": True,
                    "no-check-certificate": True,
                    "outtmpl": f"{dest}.%(ext)s",
                    "postprocessors": [{
                        "key": "FFmpegVideoConvertor",
                        "preferedformat": "mp4"
                    }],
                    "logger": Logger()
                }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def getAlbum(self, urls, dest):
        dest.mkdir(parents = True, exist_ok = True)
        count = 0

        for url in urls:
            self.getGeneric(url, dest / str(count))
            count += 1
            print(f"[Downloading album: {count}/{len(urls)}]")

    def getImgurAlbum(self, url, dest):        
        dest.mkdir(parents = True, exist_ok = True)
        dest = dest / "src.zip"

        session = requests.Session()
        ua = UserAgent().random
        headers = {
            "User-Agent": ua,
            "Referer": url
        }

        url += "/zip"
        response = session.get(url, headers = headers)

        with open(dest, "wb") as f:
            f.write(response.content)
        unzip(dest, dest.parent)

        # with requests.get(url, headers = headers, stream = True) as r:
        #     r.raise_for_status()
        #     with open(dest, "wb") as f:
        #         for chunk in r.iter_content(chunk_size = 1024 * 1024 * 1): # 1 MB
        #             f.write(chunk)

class Logger:
    def debug(self, msg):
        pass
    def error(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        pass