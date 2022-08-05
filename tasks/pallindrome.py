
def getReverse(stringx):
    l = len(stringx)
    reverse = ""
    for i in range(1,l+1):
        reverse = reverse + stringx[-i]
    return reverse

def checkPalindrome(stringy):
    if stringy == getReverse(stringy):
        print("{} is a pallindrom".format(stringy))
    else:
        print("{} is not a pallindrom".format(stringy))


if __name__ == "__main__":
    stringx = "malayalam"
    l = len(stringx)
    reverse = ""
    for i in range(1,l+1):
        reverse = reverse + stringx[-i]
    print(reverse)

    if stringx == reverse:
        print("{} is a pallindrom".format(stringx))
    else:
        print("{} is not a pallindrom".format(stringx))


    stringx="abcd"

    l = len(stringx)
    reverse = ""
    for i in range(1,l+1):
        reverse = reverse + stringx[-i]
    print(reverse)

    if stringx == reverse:
        print("{} is a pallindrom".format(stringx))
    else:
        print("{} is not a pallindrom".format(stringx))
    checkPalindrome("mani")
    checkPalindrome("madam")
    checkPalindrome("python")