a = int(input("Enter a number: "))

if a > 0:
    print("Positive")
    if a % 2 ==0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")
    if a < -10:
        print("Too low")
    else:
        print("You can make it positive")