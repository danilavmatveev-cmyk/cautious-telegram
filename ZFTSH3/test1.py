def abra(text:str):
    index = -1
    while index >= -len(text):
        letter = text[index]
        print(letter)
        index = index - 1
abra("rambles")