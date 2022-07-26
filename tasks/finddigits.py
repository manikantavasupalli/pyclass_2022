def finddigit(n):
    temp = str(n)
    counter = 0
    for digit in temp:
        digit = int(digit)
        if digit != 0 and n % digit == 0:
            counter += 1
    return counter

    
    
total_divisions = finddigit(1024)
print(total_divisions)