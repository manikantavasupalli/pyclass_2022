students = {
   "N091001": {"std": "X", "name": "mathew", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", 
    "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 123456}, "grades": 
    {"math": 8.5, "english": 9, "social": 7.5, "science": 8.0}}, 

    "N091002": {"std": "X", "name": "Mob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", 
    "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 223456}, "grades": 
    {"math": 3.5, "english": 8, "social": 6.5, "science": 8.6}}, 

   "N091003": {"std": "X", "name": "Bob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", 
    "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 323456}, "grades": 
    {"math": 6.5, "english": 7, "social": 8.5, "science": 7.5}},

   "N091004":  {"std": "X", "name": "Rob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", 
    "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 423456}, "grades": 
    {"math": 7.0, "english": 7.5, "social": 7.0, "science": 8.0}},

    "N091005": {"std": "X", "name": "Xob", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", 
    "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 523456}, "grades": 
    {"math": 9, "english": 6, "social": 8.0, "science": 7.0}},

    "N091006": {"std": "X", "name": "Mike", "class": "gamma10", "weight":50, "weight_unit": "kg", "height": 5.7, "height_unit":"feet", 
    "address": {"door": "44-10-12/123", "street": "streetx", "city": "lasangels", "zipcode": 623456}, "grades": 
    {"math": 7.2, "english": 8.5, "social": 7.5, "science": 4.5}}

}


# get the address of Xob
# l =[1,2,34]
# d = {'a': "mani", 'b': 2, 'c':3}
# print(d['b'])

for stundent in students:
    grades = (students[stundent]['grades'])
    PASS = True
    for subject in grades:
        if grades[subject] < 5:
            PASS = False
    print("Student: {}, Pass status: {}".format(students[stundent]['name'], PASS))