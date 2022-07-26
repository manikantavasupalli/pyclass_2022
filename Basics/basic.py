print("Hello world!")
# compilation
# interpretation


# compiled programming languages--- entire program file would convert into machine level code
#     1. javac a.java -> a.class
#     2. java a.class -> Output

# Interpreted programming lang --  Here line by line code gets compiled and same time its get Executed 
#     1. python a.py
#           picks line by line and it compiles and executes

# Variable creation
# variable_name = value

#string: any word or name. it should be enclosed with quotes
name = "mani"
name = "Python"
#number or integer. any simple number without decimal points
age = 26
#float. Number with floating points
temperature = 98.6
#boolean True or False
isrich = True
isSick = False
print(name)
print(age)
print(age+100)


# To get the type of variable 

print(type(name))
print(type(age))
print(type(temperature))
print(type(isrich))
print(type(isSick))

# Simple variable vs List
color1 = "orange"
color2 = "red"
color3 = "green"
color4 = "yellow"

colors = [ "orange", "red", "green", "yellow" , 100]
print(colors)
# get the length of list: len(list_name)
print(len(colors))
# refering with forward indexing: index starts with 0 and goes increased: 0..1..2..n
print(colors[0])
print(colors[1])

# refering with backward/reverse indexing: index starts with -1 and goes decreased: -1..-2..-n
print(colors[-1])
print(colors[-2])

# Slicing: Getting a slice/portion of list as new list
print(colors[3:4])  #0,1,2

student_info = ["rob", "20", "10th","100", "classx", "cityx","doorx", "contx123t7x"]
print(student_info[5])

# Dictionary: {"key": value}

xdict = { "age": 20,"name": "rob", "class": "classX", "address": {"door":123, "area": "areax", "city": "cityx", "zipcode": 123456}, "classes":["math","science", "arts", "sports"], "languages":["english", "hindi", "blah"]}

#refrer a value in dictionary, we have to use the key bases reference  dict["keyname"]
print(xdict["address"])

# to refer nested dict:
print(xdict["address"]["zipcode"])

# to refert list value in dict:
print(xdict["languages"][0])








