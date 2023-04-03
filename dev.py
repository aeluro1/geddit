import json
import pprint

with open("data/posts.json") as f:
    dump = json.load(f)

list = set()
for item in dump:
    list.add(dump[item]["type"])

pprint.pprint(list)