# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    num_letters = 0
    num_numbers = 0
    num_upper = 0
    num_lower = 0
    num_special = 0 # number of special characters
    if len(password) <= 12 and len(password) >=6: # check length of password so that it's <= 12 and >= 6
        for n in password:
            if n.isalpha():
                num_letters = num_letters + 1
                if n.isupper():
                    num_upper = num_upper + 1
                elif n.islower():
                    num_lower = num_lower + 1
            elif n.isdigit():
                num_numbers = num_numbers + 1
            else:
                num_special = num_special + 1
    else:
        return False
    print(num_letters, num_lower, num_numbers, num_special, num_upper)
    if num_numbers > 0 and num_upper >0 and num_lower >0 and num_special > 0:
        return True
    else:
        return False

print(check_password("Moshimo12@"))