# use keys from set into dictionary

s = {'a','b','c'}

val = 10

d = dict.fromkeys(s, val)

print(d)


# getting values by keys

print(d['a'])
print(d.get('a'))

print(d.items()) # item is nothing but key and value pair... gives you as tuple (key, value)

print(d.keys()) # it returns all the keys in the dictionary as list

print(d.values())  # it returns all the values in the dictionary as list

print(d.popitem())
print(d)


marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

print(marks)
marks.update(internal_marks)
print(marks)


students = { 
    "N091001": {"std": "X", "name": "mathew", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 123456}, "grades": {"math": 8.5, "english": 9, "social": 7.5, "science": 8.0}}, 
    "N091002": {"std": "X", "name": "Mob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 223456}, "grades": {"math": 7.5, "english": 8, "social": 6.5, "science": 8.6}}, "N091003": {"std": "X", "name": "Bob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 323456}, "grades": {"math": 6.5, "english": 7, "social": 8.5, "science": 7.5}}, "N091004":  {"std": "X", "name": "Rob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 423456}, "grades": {"math": 7.0, "english": 7.5, "social": 7.0, "science": 8.0}}, "N091005": {"std": "X", "name": "Xob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 523456}, "grades": {"math": 9, "english": 6, "social": 8.0, "science": 7.0}}, "N091006": {"std": "X", "name": "Mike", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 623456}, "grades": {"math": 7.2, "english": 8.5, "social": 7.5, "science": 8.5}} }

for i in students:
    if students[i]["grades"]["english"] >=8:
        print(students[i]["name"], students[i]["grades"]["english"])