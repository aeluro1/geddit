# This script will remove all items located in the data/_BIN folder from the saved registry.
# Use this when the program downloads an incorrect file, and a new update has rectified this behavior

from pathlib import Path
import json

home = Path(__file__).resolve().parents[1]
bin = home / Path("data/_BIN")
bin.mkdir(parents = True, exist_ok = True)

posts = home / Path("data/posts.json")
with open(posts) as f:
    data = json.load(f)

print(f"Total: {len(data)}")
count = 0
for item in bin.iterdir():
    try:
        id = item.name.split(" ")[0]
        if id in data:
            data.pop(id)
            print(f"{id} removed")
            count += 1
    except Exception:
        continue
print(f"Total {count} removed")

if count == 0:
    exit()

newPosts = posts.with_suffix(".old")
if newPosts.is_file():
    newPosts.unlink()
posts.rename(newPosts)

with open(posts, "w") as f:
    json.dump(data, f, indent = 4)