import string



class SEncrypt():

    ALPHABETS = string.ascii_lowercase
    ALPHABETS_LENGHT = len(ALPHABETS)
    spaceIndex = []

    def __init__(self, data, encrypt=None, decrypt=None):
        self.encrypt = encrypt
        self.decrypt = decrypt
        self.data = data
        self.done = False

    
    def removeSpace(self):
        if " " in self.data:
            self.spaceIndex = [counter for counter, element in enumerate(self.data) if element == " "]
            return self.data.replace(" ", "")
        return self.data

    def addSpace(self):
        for c, element in enumerate(self.spaceIndex):
            list(self.data).insert(element, " ")
        self.clearSpaceIndex()
        return self.data

    def clearSpaceIndex(self):
        self.spaceIndex.clear() 

    def keyFill(self, key, dataLength, keyLength):
        newKey = ""
        for r in range(dataLength-keyLength):
            for i in key: 
                if len(newKey) < dataLength:
                    newKey += i
        return newKey
    
    def vigenereCipher(self, message, key):
        finalData = []
        message = self.removeSpace(message) #remove whitespace
        newKey = self.keyFill(key, len(message), len(key)) #key fill
        for letter in range(len(message)):
            cipherIndex = self.ALPHABETS.index(message[letter]) + self.ALPHABETS.index(newKey[letter])
            cipherIndexOverflow = abs(self.ALPHABETS_LENGHT - cipherIndex)
            if cipherIndex < self.ALPHABETS_LENGHT:
                finalData.append(self.ALPHABETS[cipherIndex])
            else:
                finalData.append(self.ALPHABETS[cipherIndexOverflow])
        finalData = addSpace(finalData)
        return "".join(finalData)
    

    def vigenereDecipher(self, cipherText, key):
        global self.ALPHABETS_LENGHT
        finalData = []
        cipherText = removeSpace(cipherText)  #remove whitespace
        newKey = keyFill(key, len(cipherText), len(key)) #key fill
        for c in range(len(cipherText)):
            msgIndex = alphabets.index(cipherText[c]) - alphabets.index(newKey[c])
            msgIndexOverflow = abs(msgIndex - (self.ALPHABETS_LENGHT-1))
            if msgIndex < 0:
                msgIndex = msgIndex + self.ALPHABETS_LENGHT # +26 if msgIndex is negative
                finalData.append(alphabets[msgIndex])
            elif msgIndex <= (self.ALPHABETS_LENGHT-1) and msgIndex >= 0: #0 <= msgIndex <= 25
                finalData.append(alphabets[msgIndex])
            else: # pick from index value
                finalData.append(alphabets[abs(msgIndexOverflow)-1])
        finalData = addSpace(finalData)
        return "".join(finalData)


if __name__ == "__main__":
    se = SEncrypt("Hello there just testing new sentence")
    print(se.spaceIndex)
    print(se.removeSpace())
    print(se.spaceIndex)
    print(se.addSpace())