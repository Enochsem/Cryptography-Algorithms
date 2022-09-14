import string

alphabets = string.ascii_lowercase
alphabetsLenght = len(alphabets)



def shift3(message,key):
    keyIndex = alphabets.index(key)
    final =[]
    message = list(message)
    for letter in range(len(message)):
        if message[letter] != " ":
            letterIndex = alphabets.index(message[letter])
            cipherIndex = letterIndex + keyIndex
            indexOverflow = (len(alphabets)-1) -  cipherIndex
            if cipherIndex <= len(alphabets)-1:
                ciphertext = alphabets[cipherIndex]
                final.append(ciphertext.lower())
            else:
                ciphertext = alphabets[abs(indexOverflow)-1] # pick from index value
                final.append(ciphertext.lower())
        else:
            final.append(" ")
    return "".join(final)


def shift3decrypt(ciphertexts,key): # m=ciphertext
    keyIndex = alphabets.index(key)
    final =[]
    ciphertexts = list(ciphertexts)
    for letter in range(len(ciphertexts)):
        if ciphertexts[letter] != " ":
            letterIndex = alphabets[::-1].index(ciphertexts[letter]) #pick from the reversed letters
            cipherIndex = letterIndex + keyIndex
            lettersLeft = (len(alphabets)-1) -  cipherIndex
            if cipherIndex <= len(alphabets)-1:
                message = alphabets[::-1][cipherIndex]
                final.append(message.lower())
            else:
                message = alphabets[::-1][abs(lettersLeft)-1] # pick from index value
                final.append(message.lower())
        else:
            final.append(" ")
    return "".join(final)



#breaking down the above

def physicalShift(message,key):
    keyIndex = alphabets.index(key)
    final = []
    message = list(message)
    for letter in range(len(message)):
        if message[letter] != " ":
            letterIndex = alphabets.index(message[letter])
            cipherIndex = letterIndex + keyIndex
            indexOverflow = (alphabetsLenght-1) -  cipherIndex
            final.extend(cipherShift(indexOverflow, cipherIndex))
        else:
            final.append(" ")
    return "".join(final)


def cipherShift(indexOverflow,cipherIndex):
    result = []
    if cipherIndex <= (alphabetsLenght-1): #checing max index
        ciphertext = alphabets[cipherIndex]
        result.append(ciphertext.lower())
    else:
        ciphertext = alphabets[abs(indexOverflow)-1] # pick from index value
        result.append(ciphertext.lower())
    return result
            




msg = shift3("department of computer science", "j")
print("h:",msg)
msgph = physicalShift("department of computer science", "j")
print("ph:",msgph)
#print(shift3decript(msg, "j"))
