import string

letters = string.ascii_lowercase


#print(list(enumerate(letters)))

# print(list(enumerate(letters))[1])

spaceIndex = []
def removeSpace(data):
        if " " in data:
            for counter, element in enumerate(data):
                if element == " ":
                    spaceIndex.append(counter)
            return data.replace(" ","")
        return data

def removeSpace1(data):
    global spaceIndex
    if " " in data:
        spaceIndex = [counter for counter, element in enumerate(data) if element == " "]
        return data.replace(" ", "")
    return data

removeSpace1("hellow just testing this")
print(spaceIndex)