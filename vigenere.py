import string

alphabets =  string.ascii_lowercase
alphabetsLength = len(alphabets)

spaceIndex = []
def removeSpace(data):
    if " " in data:
        for i in range(len(data)):
            if data[i] == " ":
                spaceIndex.append(i)
        return data.replace(" ","")
    return data

def addSpace(data):
    for i in range(len(spaceIndex)):
        data.insert(spaceIndex[i], " ")
    clearSpaceIndex()
    return data

def clearSpaceIndex():
    spaceIndex.clear()

def keyFill(key, dataLength, keyLength):
    newKey = ""
    for r in range(dataLength-keyLength):
        for i in key: 
            if len(newKey) < dataLength:
                newKey += i
    return newKey

def vigenereCipher(message, key):
    finalData = []
    message = removeSpace(message) #remove whitespace
    newKey = keyFill(key, len(message), len(key)) #key fill
    for letter in range(len(message)):
        cipherIndex = alphabets.index(message[letter]) + alphabets.index(newKey[letter])
        cipherIndexOverflow = abs(alphabetsLength - cipherIndex)
        if cipherIndex < alphabetsLength:
            finalData.append(alphabets[cipherIndex])
        else:
            finalData.append(alphabets[cipherIndexOverflow])
    finalData = addSpace(finalData)
    return "".join(finalData)

def vigenereDecipher(cipherText, key):
    global alphabetsLength
    finalData = []
    cipherText = removeSpace(cipherText)  #remove whitespace
    newKey = keyFill(key, len(cipherText), len(key)) #key fill
    for c in range(len(cipherText)):
        msgIndex = alphabets.index(cipherText[c]) - alphabets.index(newKey[c])
        msgIndexOverflow = abs(msgIndex - (alphabetsLength-1))
        if msgIndex < 0:
            msgIndex = msgIndex + alphabetsLength # +26 if msgIndex is negative
            finalData.append(alphabets[msgIndex])
        elif msgIndex <= (alphabetsLength-1) and msgIndex >= 0: #0 <= msgIndex <= 25
            finalData.append(alphabets[msgIndex])
        else: # pick from index value
            finalData.append(alphabets[abs(msgIndexOverflow)-1])
    finalData = addSpace(finalData)
    return "".join(finalData)
        

cipherText = vigenereCipher("system security and control", "security")
#kcunvu lcuytckg tlv gqhkzhj
vigenereDecipher(cipherText, "security")
#system security and control