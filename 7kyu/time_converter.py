"""
Given a time in a time format class, return it without year, month and day.

It should return a string including milliseconds with 3 decimals.

Example:

datetime(2016, 2, 8, 16, 42, 59)
#Should return: 
"16:42:59,000"

"""


def convert(time):
    microseconds = time.strftime("%f")
    return time.strftime(f"%H:%M:%S,{microseconds[0:3] if len(microseconds) > 2 else '000'}")