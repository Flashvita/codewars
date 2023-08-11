

"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.
"""


def pig_it(text):
    sentence = ""
    for word in text.split(" "):
        if word in ["!", "?", "."]:
            sentence += f"{word} "
        else:
            sentence += f"{word[1::]}{word[0]}ay "
    return sentence[0:-1]


print(pig_it("Pig latin is cool"))