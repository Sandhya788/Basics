incorrectPassword= True
while incorrectPassword:
    password = input("type in your password: ")
    if len(password) < 8:
        print("your password must be 8 characters long")
    elif not any(i.isdigit() for i in password):
        print("you need a number in your password")
    elif not any(i.isupper() for i in password):
        print("you need a capital letter in your password")
    elif not any(i.islower() for i in password):
        print("you need a lowercase letter in your password")
    else:
        incorrectPassword = False