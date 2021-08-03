import re

def checkPassword(password):
    """
    Validate the password
    """
    if len(password) < 8:
        # Password to short
        print("Your password must be 8 characters long.")
        return False
    elif not re.findall(r'\d+', password):
        # Missing a number
        print("You need a number in your password.")
        return False
    elif not re.findall(r'[A-Z]+', password):
        # Missing at least one capital letter
        print("You need a capital letter in your password.")
        return False
    else:
        # All good
        print("All good")
        return True

# Promt user to enter valid password
passwordValid = False
while not passwordValid:
    password = input("Type in your password: ")
    passwordValid = checkPassword(password)