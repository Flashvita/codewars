"""
Your task in order to complete this Kata is to write a function which formats a duration,
 given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, 
it just returns "now". Otherwise, the duration is expressed
 as a combination of years, days, hours, minutes and seconds.

    -It is much easier to understand with an example:
        * For seconds = 62, your function should return 
            "1 minute and 2 seconds"
        * For seconds = 3662, your function should return
            "1 hour, 1 minute and 2 seconds"

"""

    
def format_duration(seconds):
    if seconds == 0:
        return "now"
    data = dict(years=365*24*3600, days=24*3600, hours=3600, minutes=60, seconds=1)
    message = []
    for key, value in data.items(): 
        if time := seconds // value:
            seconds -= time * value
            key = key if time != 1 else key[:-1]
            message.append(f"{time} {key}")
    if len(message) == 0:
        return message
    return "".join([", ".join(message[:-1]), " and ", message[-1]]) if len(message) > 1 else message[0]



print('res1', format_duration(1))
print('res2', format_duration(3600))
print('res3', format_duration(3601))
print('res3', format_duration(3667))
print('res3', format_duration(120))
print('res4', format_duration(171))