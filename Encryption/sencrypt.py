import string



class SEncrypt():

    ALPHABETS = string.ascii_lowercase
    ALPHABETS_LENGHT = len(ALPHABETS)
    spaceIndex = []
    finalData = []

    def __init__(self, data, encrypt=None, decrypt=None):
        self.encrypt = encrypt
        self.decrypt = decrypt
        self.data = data
        self.done = False

    
    def removeSpace(self, data):
        if " " in data:
            self.spaceIndex = [counter for counter, element in enumerate(data) if element == " "]
            return data.replace(" ", "")
        return data

    def addSpace(self,data):
        for c, element in enumerate(self.spaceIndex):
            data.insert(element, " ")
        self.clearList(self.spaceIndex)
        return data

    def clearList(self,listData):
        listData.clear() 

    def keyFill(self, key, dataLength, keyLength):
        newKey = ""
        for r in range(dataLength-keyLength):
            for i in key: 
                if len(newKey) < dataLength:
                    newKey += i
        return newKey
    
    def vigenereCipher(self, key):
        message = self.removeSpace(self.data) #remove whitespace
        newKey = self.keyFill(key, len(message), len(key)) #key fill
        for letter_index_count, letter in enumerate(message):
            #Adding letter index to newkey letter index (generates new index for a letter)
            cipherIndex = self.ALPHABETS.index(message[letter_index_count]) + self.ALPHABETS.index(newKey[letter_index_count])
            cipherIndexOverflow = abs(self.ALPHABETS_LENGHT - cipherIndex)
            if cipherIndex < self.ALPHABETS_LENGHT:
                self.finalData.append(self.ALPHABETS[cipherIndex])
            else:
                self.finalData.append(self.ALPHABETS[cipherIndexOverflow])
        return "".join(self.addSpace(self.finalData))
    

    def vigenereDecipher(self, cipherText, key):
        self.clearList(self.finalData)
        cipherText = self.removeSpace(cipherText)  #remove whitespace
        newKey = self.keyFill(key, len(cipherText), len(key)) #key fill
        for c, element in enumerate(cipherText):
            msgIndex = self.ALPHABETS.index(cipherText[c]) - self.ALPHABETS.index(newKey[c])
            msgIndexOverflow = abs(msgIndex - (self.ALPHABETS_LENGHT-1))
            if msgIndex < 0:
                msgIndex = msgIndex + self.ALPHABETS_LENGHT # +26 if msgIndex is negative
                self.finalData.append(self.ALPHABETS[msgIndex])
            elif msgIndex <= (self.ALPHABETS_LENGHT-1) and msgIndex >= 0: #0 <= msgIndex <= 25
                self.finalData.append(self.ALPHABETS[msgIndex])
            else: # pick from index value
                self.finalData.append(self.ALPHABETS[abs(msgIndexOverflow)-1])
        return "".join(self.addSpace(self.finalData))

    
    # shift cipher
    def encrypt(self,message, key):
        cipherText = []
        message = self.removeSpace(message)
        self.ALPHABETS = list(string.ascii_lowercase)
        for i in message.lower():
            for letter in self.ALPHABETS:
                if letter == i:
                    letter_index = self.ALPHABETS.index(letter)
                    result = (letter_index + key) % 26
                    cipherText.append(result)
        return cipherText

    def getText(self,cipherNumber):
        cipherText = []
        self.ALPHABETS = list(string.ascii_lowercase)
        for letter_number in cipherNumber:
            result = self.ALPHABETS[letter_number]
            cipherText.append(result)
        return "".join(cipherText)


if __name__ == "__main__":
    se = SEncrypt("system security and control")
    cipher = se.vigenereCipher("security")
    print(cipher)
    print(se.vigenereDecipher(cipher, "security"))