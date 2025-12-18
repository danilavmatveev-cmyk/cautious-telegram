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


