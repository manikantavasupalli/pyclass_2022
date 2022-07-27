import yaml

with open("/Users/i1179/personal/practice/py-class/File_ops/yaml_parse/stundent.yaml", "r") as fd:
    ydict = yaml.load(fd)
    print(type(fd))
    print(type(ydict))
    print(ydict)