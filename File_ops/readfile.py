

from asyncore import file_dispatcher


# open method takes filename and mode of openinging file 
# Modes:
#     read: r # it just reads the file
#     write: w # to writed the data into a file
#     append: a # to add the data at end
#     +: r+ or w+ it gives both read and write
#
# Methods:
#    read() # this methods reads the whole file as string "line1\nline2\nline3"
#    readline() # it reads line by line ... "line1"..."line2"
#    readlines() # this reads all the file at once and give you a list ["line1", "line2", "linen"]

fd = open("/Users/i1179/personal/practice/py-class/File_ops/inp.txt", "r")
print(fd.read())
print(fd.readline())
print(fd.readlines())
fd.close()
