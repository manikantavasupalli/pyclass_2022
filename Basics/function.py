def greet(name, counter):
    print("Hey {} ... How are you doing".format(name))
    if counter < 10:
        greet("Mani", counter+1)



greet("Rob", 0)