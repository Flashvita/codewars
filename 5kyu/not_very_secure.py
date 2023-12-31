"""
In this example you have to validate if a user input string is alphanumeric.
The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore


"""

import re

def alphanumeric(password):
    return True if re.fullmatch(r'\w+', password) else False  

print(alphanumeric("43534h56jmTHHF3k"))

# Best practice use https://pythonstart.ru/string/isalnum-python?ysclid=ll5i73w5un777934615