import json
import pprint

list = {}
with open("data/failed.json") as f:
    items = json.load(f)
for item in items:
    key = items[item]["source"]
    list[key] = list.get(key, 0) + 1

pprint.pprint(list)