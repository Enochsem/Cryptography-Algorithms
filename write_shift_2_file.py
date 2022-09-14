'''
shift cypher
Enc k => Ek(m) = m+k mod 26
Dec k => Dk(c) = c-k mod 26
'''

import string

alphabets = list(string.ascii_lowercase)

def getIndex(m):
    return alphabets.index(m)
            
def getLetter(index):
    return alphabets[index]

def writeToFile(solution):
    with open("Cryptograpy.txt","a") as assignment:
        assignment.write(solution)
        
def Ek(m,k):
    cipherText = []
    for i in m.lower():
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = getIndex(letter)
                    step1 = "Ek(m) = m+k mod 26"
                    step2= f"E{k}({i}) = {i} + {k} mod 26"
                    step3 =f"E{k}({i}) = {letter_index} + {k} mod 26"
                    step4 = f"E{k}({i}) = {letter_index + k} mod 26"
                    step5 = f"E{k}({i}) = {(letter_index + k) % 26}"
                    step6 = f"E{k}({i}) = {getLetter((letter_index + k) % 26)}"
                    solution = f"{step1}\n{step2}\n{step3}\n{step4}\n{step5}\n{step6}\n\n"
                    cipherText.append(getLetter((letter_index + k) % 26))
                    writeToFile(solution)
        else:
            cipherText.append(" ")
    return "".join(cipherText)    

def Dk(c,k):
    for i in c:
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = getIndex(letter)
                    step1 = "Dk(c) = c-k mod 26"
                    step2= f"D{k}({i}) = {i} - {k} mod 26"
                    step3 =f"D{k}({i}) = {letter_index} - {k} mod 26"
                    step4 = f"D{k}({i}) = {letter_index - k} mod 26"
                    step5 = f"D{k}({i}) = {(letter_index - k) % 26}"
                    step6 = f"D{k}({i}) = {getLetter((letter_index - k) % 26)}"
                    solution = f"{step1}\n{step2}\n{step3}\n{step4}\n{step5}\n{step6}\n\n"
                    writeToFile(solution)
                
key = 9
cipherText = Ek("code", key)
Dk(cipherText, key)



