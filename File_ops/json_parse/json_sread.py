import json
jdata = """{
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    }"""

print(type(jdata))
jdict = json.loads(jdata)
print(type(jdict))
print(jdict)
