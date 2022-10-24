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

def vigenereDecript(cipherText, key):
    global alphabetsLength
    finalData = []
    newKey = key
    cipherTextLength = len(cipherText)
    keyLength = len(key)
    cipherText2KeyOverflow = abs(cipherTextLength - keyLength)
    for r in range(cipherTextLength-keyLength):
        for i in key: #key fill
            if len(newKey) < cipherTextLength:
                newKey += i

    for c in range(cipherTextLength):
        msgIndex = abs(alphabets.index(newKey[c]) - alphabets.index(cipherText[c]))
        msgIndexOverflow = abs(msgIndex - (alphabetsLength-1))
        if msgIndex <= (alphabetsLength-1):
            msg = alphabets[msgIndex]
            finalData.append(msg)
        else:
            msg = alphabets[abs(msgIndexOverflow)-1] # pick from index value
            finalData.append(alphabets[msg])
        return "".join(finalData)
        
    

print(vigenereDecript("kcunvulcuytckg", "security"))