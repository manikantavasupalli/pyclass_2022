import yaml
import json

with open("/Users/i1179/personal/practice/py-class/File_ops/yaml_parse/stundent.yaml", "r") as fd:
    ydict = yaml.load(fd)
    print(type(fd))
    print(type(ydict))
    print(ydict)

with open("output_new.json", "w") as fd:
    json.dump(ydict, fd)