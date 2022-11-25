import string



class SEncrypt():

    ALPHABETS = string.ascii_lowercase
    ALPHABETS_LENGHT = len(self.ALPHABETS)
    spaceIndex = []

    def __init__(self, data, encrypt=None, decrypt=None):
        self.encrypt = encrypt
        self.decrypt = decrypt
        self.data = data

    
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

    def keyFill(key, dataLength, keyLength):
        newKey = ""
        for r in range(dataLength-keyLength):
            for i in key: 
                if len(newKey) < dataLength:
                    newKey += i
        return newKey

    


if __name__ == "__main__":
    se = SEncrypt("Hello there just testing")
    print(se.spaceIndex)
    print(se.removeSpace())
    print(se.spaceIndex)
    print(se.addSpace())