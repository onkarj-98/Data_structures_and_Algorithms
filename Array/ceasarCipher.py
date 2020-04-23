def cipher(string, key):
    newLetter = []
    newKey = key % 26
    for letter in string:
        newLetter.append(getNewLetter(letter, newKey))
    return "".join(newLetter)


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)  # the small case start from 97


print(cipher("onkar", 7))
