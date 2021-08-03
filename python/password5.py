incorrectPassword= True
while incorrectPassword:
    password = input("type in your password")
    if len(password < 8):
        print("your password must be 8 characters long")
    elif noNum(password == False):
        print("you need a number in your password")
    elif noCap(password == False):
        print("you need a capital letter in your password")
    elif NoLow(password == False):