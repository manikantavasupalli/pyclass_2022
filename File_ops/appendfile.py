

fd = open("a.txt", "a")
data = [ "Hi this is line1\n", "Hi this is line2\n", "Hi this is line3\n", "Hi this is line4\n" ]
fd.write("\nHi this is line0\n")
print(fd.seek(0))
fd.writelines(data)
fd.close()


with open("b.txt", "a") as fd:
    fd.write("Am new way of opening ... and will get closed as soon as with block complete")