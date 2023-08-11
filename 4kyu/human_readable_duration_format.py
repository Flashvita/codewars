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




# def get_value_time(data, key, value, seconds):
#     print('val', data, key, value, seconds)
#     if data[key] > seconds:
#         return seconds / value
#     elif key == "days":
#         return seconds % (value * 24)
#     elif key == "hours":
#         return seconds % 60
#     elif key == "seconds":
#         return seconds % 60
#     elif key == "minutes":
#         return seconds / value
#     else:
#         return 100000000000


    
# def format_duration(seconds):
#     data = dict(years=365*24*3600, days=24*3600, hours=3600, minutes=60, seconds=1)
#     human_duration = ""
#     for key, value in data.items():
#         print('key, value seconds |', key, value, seconds)
#         if seconds < value:
#             print('continue next =====>>>')
#             continue
#         #value_time = int(seconds / value if data[key] > seconds / value else seconds % 60)
#         value_time = get_value_time(data, key, value, seconds)
#         print('value_time, data[key]', value_time, data[key])
#         key_name = key[:-1] if value_time == 1 else key
#         data_string = f"{int(value_time)} {key_name}"
#         print('value_time', value_time)
#         if value_time >= 1:
#             if seconds % value == 0:
#                 if key == "seconds" and len(human_duration) > 0:
#                     human_duration  += "and "
#                 human_duration += data_string
#                 return human_duration
#             if key == "seconds" and len(human_duration) > 0:
#                     human_duration  += "and "
#             print("new time append", f"{value_time} {key_name} ")
            
#             human_duration += f"{int(value_time)} {key_name} "
#         else:
#             continue
#     return human_duration[0:-1]


# def format_duration(seconds):
#     data = dict(years=365*24*3600, days=24*3600, hours=3600, minutes=60, seconds=1)
#     human_duration = ""
#     for key, value in data.items():
#         value_time = seconds / value if value > seconds else value % seconds
#         key_name = key if value_time > 1 else key[:-1]
#         data_string = f"{int(value_time)} {key_name}"
#         print('value_time', value_time)
#         if value_time >= 1:
#             print('value_time', value_time)
#             if isinstance(value_time, float):
#                 _,  mseconds = f"{value_time}".split(".", value_time)
#             if mseconds == 0:
#                 human_duration += data_string
#                 return human_duration
#             human_duration += f"{int(value_time/value)} {key_name} "
#         else:
#             continue
#     return human_duration[0:-1]


# def prettyList(human_time):
#     if len(human_time) > 1:
#         return ' '.join([', '.join(human_time[:-1]), "and", human_time[-1]])
#     elif len(human_time) == 1:
#         return human_time[0]
#     else:
#         return ""

# def format_duration(seconds):
#     intervals = (('hours', 3600), ('minutes', 60), ('seconds', 1))
#     human_time = []
#     for name, count in intervals: 
#         value = seconds // count
#         if value: 
#             seconds -= value * count
#             if value == 1:
#                 name = name.rstrip('s')
#             human_time.append(f"{value} {name}")
#     if not human_time:
#         return "now"
#     human_time = human_time[:3]
#     return prettyList(human_time)
