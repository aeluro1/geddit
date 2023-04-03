from pathlib import Path
import requests
import youtube_dl

def download(entry, reddit):
    path = Path("data") / entry.sub

    match entry.type:
        case "i.redd.it" | "i.imgur.com" | "redgifs.com":
            response = requests.get(entry.url)
        case "v.redd.it" | "gfycat.com":
            pass
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
