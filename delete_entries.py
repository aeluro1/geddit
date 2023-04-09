# This script will remove all items located in the data/_BIN folder from the saved registry.
# Use this when the program downloads an incorrect file, and a new update has rectified this behavior

from pathlib import Path
import json

bin = Path("data/_BIN")
bin.mkdir(parents = True, exist_ok = True)

posts = Path("data/posts.json")
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
    except:
        continue
print(f"{count} removed")

posts.rename(posts.with_suffix(".old"))

with open(posts, "w") as f:
    json.dump(data, f, indent = 4)