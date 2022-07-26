from asyncio import events


x = int(input("Enter a number: "))

rem = x%2
if rem == 0:
    print("since reminder is " + str(rem) + ", " + str(x) + "  is even")
    print("Hello")
else:
    print("since reminder is {}, {} is even".format(rem, x))


# "since reminder is " + rem + ", " str(x) "  is even"


# since reminder is 0 input number is even

# since reminder is 1 input number is odd