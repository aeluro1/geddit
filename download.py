from __future__ import unicode_literals
from pathlib import Path
from mimetypes import guess_extension
from time import sleep
import json
import re

import requests
from yt_dlp import YoutubeDL

from utils import trueLink, BlankLogger


class Downloader:
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"}

    def __init__(self):
        with open("sources.json") as f:
            self._sources = json.load(f)

        self._verbose = False

    def download(self, entry, prefix):
        dest = Path("data") / entry["sub"]
        url = entry["url"]
        title = re.sub(r"[\\/*?:.\"<>|]", "", entry["title"])
        title = (prefix + " - " + title)[:250].strip()

        # Create subreddit folder if non-existent, then set 'dest' to include post file/folder
        dest.mkdir(parents = True, exist_ok = True)
        dest = dest / title
        
        exc = None

        # First, attempt to download the default URL
        try:
            self.execute(entry, url, dest)
            if self._verbose: print(f"Successfully downloaded with original URL")
            return
        except Exception as e:
            exc = e
            if self._verbose: print(e)

        # Then, attempt to download the redirected URL (usually automatic, sometimes fails)
        try:
            self.execute(entry, trueLink(url), dest)
            if self._verbose: print(f"Successfully downloaded with true URL")
            return
        except Exception as e:
            if self._verbose: print(e)

        # Then, download the image cached by Reddit if it exists
        try:
            if entry["source"] in self._sources["vid"] or isinstance(entry["data"], list):
                raise ValueError("Will not download preview image for an album or video")
            
            self.execute(entry, entry["url_preview"], dest)
            if self._verbose: print(f"Successfully downloaded with preview URL")
            return
        except Exception as e:
            if self._verbose: print(e)
        
        # Finally, locate historical URLs and attempt to download them until there are no more links
        try:
            if isinstance(entry["data"], list):
                raise RuntimeError("Wayback implementation does not support albums yet")
            
            wb_urls = self.getWayback(url)
            count = 1
            for wb in wb_urls:
                try:
                    print(f"[Attempting wayback machine download: {count}/{len(wb_urls)}]")
                    self.execute(entry, wb, dest)
                    if self._verbose: print(f"Successfully downloaded with wayback URL")
                    return
                except:
                    count += 1
                    continue
        except Exception as e:
            if self._verbose: print(e)

        raise exc

    def execute(self, entry, url, dest):
        source = entry["source"]

        # Annoyingly, some links redirect to removed data (a generic 'removed' picture) but don't return an HTTP error
        checkLink = trueLink(url)
        if any(badLink in checkLink for badLink in self._sources["invalid"]):
            raise ValueError("Bad link")

        if source in self._sources["vid"]: # Video detected
            self.getVid(url, dest)
            return

        if source in self._sources["img"]: # Image detected
            if "imgur.com/a/" in url or "reddit.com/gallery/" in url: # Fetch reddit gallery
                self.getAlbum(entry["data"], dest)
            elif url.endswith(".gifv"): # Edge case for gif "video" hosted on Reddit image site
                self.getVid(url, dest)
            else: # Generic image download
                self.getGeneric(url, dest)
            return

        if source.startswith("self."): # Text post
            self.getText(entry["data"], dest)
            return

        # Unknown post format - see if media type is encoded in HTTP response
        response = requests.head(url, headers = Downloader.headers, timeout = 30, allow_redirects = True)
        response.raise_for_status()
        mediaType = response.headers["content-type"]
        if "image" in mediaType.lower():
            self.getGeneric(url, dest)
            return
        elif "video" in mediaType.lower():
            self.getVid(url, dest)
            return
        
        raise RuntimeError(f"Unkown domain for post '{dest.name}': {source}")

    def getGeneric(self, url, dest):
        if self._verbose:
            print(f"Downloading image: {url}")

        with requests.get(url, headers = Downloader.headers, stream = True, timeout = 30) as r:
            r.raise_for_status()
            ext = guess_extension(r.headers["content-type"].split(";")[0].strip())
            dest = Path(str(dest) + ext)
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size = 1024 * 1024 * 1): # 1 MB
                    f.write(chunk)

    def getText(self, data, dest):
        if self._verbose:
            print(f"Downloading text post: {dest.name}")

        dest = Path(str(dest) + ".md")
        with open(dest, "w", encoding = "utf-8") as f:
            f.write(data)
        
    def getVid(self, url, dest):
        if self._verbose:
            print(f"Downloading video: {url}")

        ydl_opts = {
                    "quiet": True,
                    "nocheckcertificate": True,
                    "ignoreerrors": True,
                    "outtmpl": f"{dest}.%(ext)s",
                    # "postprocessors": [{
                    #     "key": "FFmpegVideoConvertor",
                    #     "preferedformat": "mp4"
                    # }],
                    "logger": BlankLogger()
                }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if not any([file.name.startswith(dest.name) for file in dest.parent.iterdir()]):
            raise RuntimeError("Failed to download video")

    def getAlbum(self, urls, dest):
        dest.mkdir(parents = True, exist_ok = True)
        count = 0

        if len(urls) == 0:
            raise ValueError("No images in album found")
        for url in urls:
            self.getGeneric(url, dest / str(count))
            count += 1
            print(f"[Downloaded album for {dest.name}: {count}/{len(urls)}]")


    def getWayback(self, url):
        if self._verbose:
            print(f"Getting information from wayback machine: {url}")

        wb_api = "https://web.archive.org/cdx/search/cdx"
        wb_src = "https://web.archive.org/web"

        params = {
            "url": url,
            "output": "json",
            "gzip": False,
            "fl": "timestamp,statuscode",
            "collapse": "digest",
        }
        response = requests.get(wb_api, headers = Downloader.headers, params = params, timeout = 30)
        if response.status_code == 429:
            print("[Wayback machine is overloaded - waiting 1 minute]")
            sleep(61)
            response = requests.get(wb_api, headers = Downloader.headers, params = params, timeout = 30)
        response.raise_for_status()

        captures = response.json()
        if len(captures) != 0:
            stamps = captures[1:]
            stamps = [stamp for stamp in stamps if stamp[1].isdigit()]
            stamps = sorted(stamps, key = lambda x: int(x[1]))
            urls = [wb_src + f"/{stamp[0]}/{url}" for stamp in stamps]
        
        return urls[:3]
    
    @property
    def verbose(self):
        return self._verbose
    
    @verbose.setter
    def verbose(self, val):
        self._verbose = val