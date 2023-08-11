"""You woke up from a massive headache and can't seem to find your car key. You find a note with a clue that says:

    "If you're reading this then I have left the state and am well on my way to freedom. Just to make things interesting, I have also provided something for you to track me with. Let the chase begin..."

Given an array of binary numbers, figure out and return the culprit's message to find out who took the missing car key.
Example:
    ['01000001', '01101100', '01100101', '01111000', '01100001', '01101110', '01100100', '01100101', '01110010'] => 
    'Alexander'

"""

def who_took_the_car_key(message):
    return "".join(chr(int(i[:8], 2)) for i in message)


print(who_took_the_car_key(['01000001', '01101100', '01100101', '01111000', '01100001', '01101110', '01100100', '01100101', '01110010']))