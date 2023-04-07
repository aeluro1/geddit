from __future__ import unicode_literals
from pathlib import Path
from mimetypes import guess_extension
import json
import re

import requests
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from utils import trueLink, BlankLogger


class Downloader:

    def __init__(self):
        with open("sources.json") as f:
            self._sources = json.load(f)

    def download(self, entry, prefix):
        dest = Path("data") / entry["sub"]
        url = entry["url"]
        title = re.sub(r"[\\/*?:.\"<>|]", "", entry["title"])
        title = (prefix + " - " + title)[:250]

        # Create subreddit folder if non-existent, then set 'dest' to include post file/folder
        dest.mkdir(parents = True, exist_ok = True)
        dest = dest / title

        try:
            self.execute(entry, url, dest)
        except:
            pass
        try:
            self.execute(entry, trueLink(url), dest)
        except:
            pass

    def execute(self, entry, url, dest):
        source = entry["source"]

        if source in self._sources["vid"]: # Video detected
            try:
                self.getVid(url, dest)
            except DownloadError as e:
                # error = e.exc_info[1].code
                # # if not error in [429, 403, 503]:
                # if error in [410, 404]: # Video is deleted, so might as well save the preview if it exists
                #     self.getGeneric(entry["url_preview"], dest)
                # else:
                #     raise e
                raise e
            return

        if source in self._sources["img"]: # Image detected
            if "imgur.com/a/" in url or "reddit.com/gallery/" in url: # Fetch reddit gallery
                self.getAlbum(entry["data"], dest)
            elif ".gifv" in url: # Edge case for gif video
                self.getVid(url, dest)
            elif "/removed." in url: # Edge case where Imgur image is deleted but Reddit cached it
                self.getGeneric(entry["url_preview"], dest)
            else: # Known image
                try:
                    self.getGeneric(url, dest)
                except:
                    self.getGeneric(entry["url_preview"], dest)
            return

        if source.startswith("self."): # Text post
            self.getText(entry["data"], dest)
            return

        try: # Unknown post format - see if media type is encoded in HTTP response
            response = requests.head(url, timeout = 5, allow_redirects = True)
            response.raise_for_status()
            mediaType = response.headers["content-type"]
            if "image" in mediaType.lower():
                self.getGeneric(url, dest)
                return
            elif "video" in mediaType.lower():
                self.getVid(url, dest)
                return
        except:
            pass

        if entry["url_preview"] != "": # Unknown post format, but it has a downloadable preview
            self.getGeneric(entry["url_preview"], dest)
            return
        
        raise Exception(f"Unkown domain for post '{dest.name}': {source}")

    def getGeneric(self, url, dest):
        with requests.get(url, stream = True, timeout = 5) as r:
            r.raise_for_status()
            ext = guess_extension(r.headers["content-type"].split(";")[0].strip())
            dest = Path(str(dest) + ext)
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size = 1024 * 1024 * 1): # 1 MB
                    f.write(chunk)

    def getText(self, data, dest):
        dest = Path(str(dest) + ".md")
        with open(dest, "w", encoding = "utf-8") as f:
            f.write(data)
        
    def getVid(self, url, dest):
        ydl_opts = {
                    "quiet": True,
                    "no-check-certificate": True,
                    "outtmpl": f"{dest}.%(ext)s",
                    # "postprocessors": [{
                    #     "key": "FFmpegVideoConvertor",
                    #     "preferedformat": "mp4"
                    # }],
                    "logger": BlankLogger()
                }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def getAlbum(self, urls, dest):
        dest.mkdir(parents = True, exist_ok = True)
        count = 0

        if len(urls) == 0:
            raise Exception("No images in album found")
        for url in urls:
            self.getGeneric(url, dest / str(count))
            count += 1
            print(f"[Downloaded album: {count}/{len(urls)}]")


    def getWayback(self, url):
        wb_api = "https://web.archive.org/cdx/search/cdx"
        wb_src = "https://web.archive.org/web"

        if url != "":
            params = {
                "url": url,
                "output": "json",
                "gzip": False,
                "fl": ["timestamp"],
                "filter": "statuscode:200",
                "collapse":"digest"
            }
            r = requests.get(wb_api, params = params)
            r.raise_for_status()
            captures = r.json()

            if len(captures) != 0:
                stamp = captures[1][0]
                url = wb_src + f"/{stamp}/{url}"
                return url