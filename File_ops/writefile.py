
fd = open("write.txt", "w+")
data = [ "Hi this is line1\n", "Hi this is line2\n", "Hi this is line3\n", "Hi this is line4\n" ]
fd.writelines(data)
fd.seek(0)
fd.write("BYE")
fd.close()
