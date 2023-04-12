# This is to remove all invalid Imgur images that were still downloaded due to the link being valid.
# Run this, then run geddit again to retrieve the correct images.

import json
from pathlib import Path

home = Path(__file__).resolve().parents[1]
path = home / Path("data/posts.json")

with open(path) as f:
    data = json.load(f)

for key in data:
    url = data[key]["url"]
    if "/removed." in url:
        print(f"Post {key} removed")
        data.pop(key)
    
with open(path, "w") as f:
    json.dump(data)