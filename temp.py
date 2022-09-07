'''
shift cypher
Enc k => Ek(m) = m+k mod 26
Dec k => Dk(c) = c-k mod 26
'''
import string

alphabets = list(string.ascii_lowercase)

def getIndex(m):
    letter_index = alphabets.index(m)
    return letter_index
            


def getLetter(index):
    return alphabets[index]


# print("hhhhhh")


"""
def ek(m,k):
    print("gggg")
    cipherText = []
    for i in m.lower():
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = getIndex(letter)
                    print("Ek(m) = m+k mod 26")
                    print(f"E{k}({i}) = {i} + {k} mod 26")
                    print(f"= {letter_index} + {k} mod 26")
                    print(f"= {letter_index + k} mod 26")
                    result = (letter_index + k) % 26
                    print(f"= {result}")
                    print(f"= {getLetter(result)}")
                    print("\n\n")
    print(cipherText)
"""

def writeToFile(solution):
    with open("Cryptograpy.txt","a") as assignment:
        assignment.write(solution)
        

def ek(m,k):
    print("ggggh")
    for i in m.lower():
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = getIndex(letter)
                    solution = f'''
Ek(m) = m+k mod 26
E{k}({i}) = {i} + {k} mod 26
    = {letter_index} + {k} mod 26
    = {letter_index + k} mod 26
    = {(letter_index + k) % 26}
    = {getLetter((letter_index + k) % 26)}
\n
'''
                    print(solution)
                    writeToFile(solution)


def dk(c,k):
    print("ddd")
    for i in c.lower():
        if i != " ":
            for letter in alphabets:
                if letter == i:
                    letter_index = getIndex(letter)
                    solution = f'''
Dk(c) = c-k mod 26
D{k}({i}) = {i} - {k} mod 26
    = {letter_index} - {k} mod 26
    = {letter_index - k} mod 26
    = {(letter_index - k) % 26}
    = {getLetter((letter_index - k) % 26)}
\n
'''
                    print(solution)
                    writeToFile(solution)


ek("de", 9)
dk("mn", 9)

'''ek("department", 9)
dk("mnyjacvnwc", 9)'''

##write to file
