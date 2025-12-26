def has_no_e():
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if "e" not in word.lower():
                return True
    return False

if has_no_e():
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if 'e' not in word.lower():
                print(word)

def avoid(word, forbidden):
    for ch in forbidden:
        if ch in word:
            return False
    return True

def uses_only(word,required):
    for ch in word:
        if ch not in required:
            return False
    return True

def uses_all(word, required):
    for ch in required:
        if ch in word:
            return False
    return True

def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


