"""Programe to solve my assignment for me  using the Formal definition"""
'''
shift cypher
Enc k => Ek(x) = x+k mod 26
Dec k => Dk(c) = c-k mod 26
'''
import string

# alphabets = list(string.ascii_lowercase)
# print(alphabets)


def encripted_numbers_to_text(cipherNumber): #old
    cipherText = []
    alphabets = list(string.ascii_lowercase)
    for letter_number in cipherNumber:
        if letter_number != " ":
            for index in range(len(alphabets)):
                if letter_number == index:
                    #print(letter_number,"==", index)
                    result = alphabets[index]
                    cipherText.append(str(result))
        else:
            cipherText.append(" ")
    return "".join(cipherText)


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

e = encrypt("Department of computer science", 9)
print(e)
#ci = encripted_numbers_to_text(e)
ci = getText(e)
print(ci)
d = decryption(ci, 9)
print("d:", d)
# di = encripted_numbers_to_text(d)
di = getText(d)
print(di)