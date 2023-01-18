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
    


if __name__ == "__main__":
    se = SEncrypt("Hello there just testing new sentence")
    print(se.spaceIndex)
    print(se.removeSpace())
    print(se.spaceIndex)
    print(se.addSpace())