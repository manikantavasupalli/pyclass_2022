a = [4,3,2,1,9]

print(len(a))
print(a.count(2))
print(a.index(2))

a.insert(5, 7)  # this method inserts the value 7 at the index 5
print(a)

a.append(8)   # this adds the value 8 at the end of the list
print(a)

print(a.pop()) # this method shows the last value from the list and also deletes from the list
print(a)

a.sort()  # this method sorts the list in ascending order
print(a)

a.reverse() # this method does updates the list in reverse order
print(a)

a.remove(7) # this method removes the value 7 from the list
print(a)

temp = [0,-1]
a.extend(temp)  # a = a + temp
print(a)


print(a.pop(4)) # here pop picks the 4th index value and removes it
print(a)

del a[0]  # similar to pop. it removes the 0th index value from the list
print(a)

a.clear() # it removes all the values from the list
print(a)

