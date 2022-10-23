import string

alphabets =  string.ascii_lowercase
alphabetsLength = len(alphabets)

def vigenereCipher(message, key):
    finalData = []
    newKey = key
    messageLength = len(message)
    keyLength = len(key)
    message2KeyOverflow = abs(messageLength - keyLength)
    for r in range(messageLength-keyLength):
        for i in key: #key fill
            if len(newKey) < messageLength:
                newKey += i

    for letter in range(messageLength):
        cipherIndex = alphabets.index(message[letter]) + alphabets.index(newKey[letter])
        cipherIndexOverflow = abs(alphabetsLength - cipherIndex)
        if cipherIndex < alphabetsLength:
            cipherText = alphabets[cipherIndex]
            finalData.append(cipherText)
        else:
            cipherText = alphabets[cipherIndexOverflow]
            finalData.append(cipherText)
    return "".join(finalData)


#system security and control
#kcunvu lcuytckg tlv gqhkzhj

#print(vigenereCipher("systemsecurity", "security"))

def vigenereDecript():
    pass