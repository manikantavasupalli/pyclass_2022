import json

with open("/Users/i1179/personal/practice/py-class/File_ops/json_parse/sample.json", "r") as jd:
    print(type(jd))
    jdict = json.load(jd)

print(type(jdict))
print(jdict["members"][1].keys())