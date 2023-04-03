import requests

def toAscii(str):
    """Helper function to remove unicode characters from string

    Args:
        str (str): String to filter

    Returns:
        str: Filtered string
    """
    return str.encode("ascii", "ignore").decode()

def download(url, dest):
    try:
        with requests.get(url, stream = True) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size = 1024 * 1024 * 1): # 1 MB
                    f.write(chunk)
        return True
    except:
        print(f"Could not download {url}")
        return False