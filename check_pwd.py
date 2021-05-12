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
    return True
