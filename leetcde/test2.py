def has_no_e(word):
    for letter in word.lower:
        if letter == 'e':
            return False
    return True

if has_no_e():
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if 'e' not in word.lower():
                print(word)



