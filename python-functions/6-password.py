def check_length(password): # a function to check the length of the password
    if len(password) < 8:
        return False
    return True

def check_others(password): # checks if password contains any uppercase, lowercase letters and a digit
    upper = False
    lower = False
    digit = False

    for i in range(len(password)):
        if (password[i].isupper()): # checks for uppercase letters 
            upper = True
        
        if (password[i].lower()): # checks for lowercase letters
            lower = True
        
        if password[i].isdigit(): # checks for digit 
            digit = True

    if upper & lower & digit != True:
        return False
       
    return True

def check_spaces(password): # checks that the password has no spaces
    if password.find(" ") != -1: # if spaces found, return False
        return False
    return True


def validate_password(password):
    length = check_length(password)
    space = check_spaces(password)
    others = check_others(password)

    if length & space & others != True:
        return False

    return True

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))