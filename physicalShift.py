import string

alphabets = string.ascii_lowercase
alphabetsLenght = len(alphabets)
reversedAlphabet = alphabets[::-1] #reversed alphabet
       
def getAlphabet(enc):
    if enc=="enc":
        alphabet = alphabets
    elif enc == "dec":
        alphabet = reversedAlphabet
    return alphabet

def physicalShift(text, key, enc = "enc"): # m=ciphertext
    messageAlphabet = getAlphabet(enc)
    keyIndex = alphabets.index(key) #get key index
    final =[]
    text = list(text.lower())
    for letter in range(len(text)):
        if text[letter] != " ":
            letterIndex = messageAlphabet.index(text[letter]) #get index of letter
            shiftIndex = letterIndex + keyIndex #get new text index
            lettersLeft = (alphabetsLenght-1) -  shiftIndex #get index overflow
            final.extend(shift(lettersLeft, shiftIndex, messageAlphabet))
        else:
            final.append(" ")
    return "".join(final)

def shift(lettersLeft,shiftIndex, messageAlphabet): #
    result = []
    if shiftIndex <= (alphabetsLenght-1): #checking max index overflow
        message = messageAlphabet[shiftIndex] #shift letter
        result.append(message)
    else:
        message = messageAlphabet[abs(lettersLeft)-1]  #shift letter
        result.append(message)
    return result
            
key = "j"
cipher = physicalShift("department of computer science", key)
#Cyper text: mnyjacvnwc xo lxvydcna blrnwln
physicalShift(cipher, key, "dec") # pass in dec to decript the cipher text
#Plain text: department of computer science



