def has_no_e():
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if "e" not in word.lower():
                return True
    return False

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

def pairs_letters(word):
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            return True
    return False


def has_three_consecutive_pairs(word):

    if len(word) < 6:
        return False

    pair_count = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            pair_count += 1
            if pair_count == 3:
                return True
            i += 2
        else:
            pair_count = 0
            i += 1

    return False


def three_pairs_letters():
    """Находит все слова с тремя парами одинаковых букв подряд"""
    with open('words.txt') as fin:
        words = [line.strip() for line in fin]

    result = []
    for word in words:
        if has_three_consecutive_pairs(word):
            result.append(word)
    return result