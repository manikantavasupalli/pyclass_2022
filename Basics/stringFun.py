st = "MacinthosMacos123"


print(st)
print(st.capitalize())
print(st.center(11, '*'))
print(st.casefold())
print(st.count('M'))
print(st.casefold().count('m'))
print(st.endswith('Macos'))
print(st.expandtabs())

a = st.encode()
print(st.encode())
print(a.decode(encoding='ascii'))
print(st.find("X"))
print("Hi i have {} laptop {}".format(st, "how about you?"))
print(st.index('os'))
print(st.isalnum())
print(st.isalpha())
print("12345".isdecimal())

temp = "12345000a"
if temp.isnumeric():
    print(int(temp) + 200)
else:
    print("{} is not a digit to convert into int".format(temp))


print(st.lower())
print("mani123".isidentifier())
print(st.split('s'))
print("  ma ni\n".strip())
print(st.replace("Macos", "Windows"))

