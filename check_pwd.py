# Andre Ortega
# TDD

# check_pwd accepts a string and returns True if it meets the following criteria:
#   Must be between 8 and 20 characters (inclusive)
#   Must contain at least one lowercase letter
#   Must contain at least one uppercase letter
#   Must contain at least one digit
#   Must contain at least on symbol from    ~`!@#$%^&*()_+-=

def check_pwd(string):

    if len(string) < 8 or len(string) > 20:
        return False

    flag1 = 0 # checks for uppercase
    flag2 = 0 # checks for lowercase
    flag3 = 0 # checks for digit
    flag4 = 0 # checks for special characters

    for element in string:
        if element.isupper():
            flag1 = 1
        if element.islower():
            flag2 = 1
        if element.isdigit():
            flag3 = 1

    # Cited idea from Kite.com
    specials = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="]
    matched_specials = [characters in specials for characters in string]
    for boolean in matched_specials:
        if boolean == True:
            flag4 = 1

    if flag1 == 0 or flag2 == 0 or flag3 == 0 or flag4 == 0:
        return False

    return True

# Cited works:
    # 1. https://www.kite.com/python/answers/how-to-check-if-a-string-contains-certain-characters-in-python
