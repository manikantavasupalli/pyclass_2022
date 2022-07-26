
def getMypay():
    # connect to so db and gives result
    return [100, "dollar"]

def toRupee(amount, currentformat):
    if currentformat == "dollar":
        amount_inr = amount * 75
    return amount_inr

def update_db(user, amount):
    # connects db and update amount
    print("User {} salary is successfully updated in the database".format(user))

payment_x = getMypay()
print(payment_x)
payment_inr = toRupee(payment_x[0], payment_x[1])
update_db("xyz", payment_inr)


