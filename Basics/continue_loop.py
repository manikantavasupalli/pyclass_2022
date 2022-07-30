
# x = 0
# while x < 11:
#     x = x + 1
#     if x%2 == 0:
#         continue
#     print(x)
#     print("Hi this is while and testing continue")
#     print("seems its odd iteration... continue instruction skips the further execution in the iteration")


for i in range(1,10):
    if i%2 != 0:
        continue
    print(i)
    print("Hi this is while and testing continue")
    print("seems its even iteration... continue instruction skips the further execution in the iteration")
    