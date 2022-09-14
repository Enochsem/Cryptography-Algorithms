import string

def encrypt(message, key):
    cipherText = []
    alphabets = list(string.ascii_lowercase)
    for i in message.lower():
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = alphabets.index(letter)
                    result = (letter_index + key) % 26
                    cipherText.append(result)
        else:
            cipherText.append(" ")
    return cipherText


def getText(cipherNumber):
    cipherText = []
    alphabets = list(string.ascii_lowercase)
    for letter_number in cipherNumber:
        if letter_number != " ":
            result = alphabets[letter_number]
            cipherText.append(result)
        else:
            cipherText.append(" ")
    return "".join(cipherText)


def decryption(cipherText, key):
    plainText = []
    alphabets = list(string.ascii_lowercase)
    for i in cipherText.lower():
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = alphabets.index(letter)
                    result = (letter_index - key) % 26
                    plainText.append(result)
        else:
            plainText.append(" ")
    return plainText


key = 9
cipherNumbers = encrypt("Department of computer science", key)
#[12, 13, 24, 9, 0, 2, 21, 13, 22, 2, ' ', 23, 14,' ',...
getText(cipherNumbers)
#cipher Text: mnyjacvnwc xo lxvydcna blrnwln
textNumbers = decryption(ci, key)
#[3, 4, 15, 0, 17, 19, 12, 4, 13, 19, ' ', 14, 5, ' ',...
getText(textNumbers)
#plane Text: department of computer science


