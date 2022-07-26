def checkeven(number):
    rem = number%2
    if rem == 0:
        print("since reminder is " + str(rem) + ", " + str(number) + "  is even")
        print("Hello even")
    else:
        print("since reminder is {}, {} is even".format(rem, number))    
        print("Hello odd") 
    print("Thank you for calling checkeven function/method")



x = int(input("Enter a number: "))
checkeven(x)
print("Function completed")

# "since reminder is " + rem + ", " str(x) "  is even"


# since reminder is 0 input number is even

# since reminder is 1 input number is odd