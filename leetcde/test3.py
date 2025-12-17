def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find("кракозябраб","б",3))

def count (word,letter):
    c = 0
    for letter in word:
        if letter == 'а':
            c = c + 1
    return (c)
print(count("ракозябра", "а"))