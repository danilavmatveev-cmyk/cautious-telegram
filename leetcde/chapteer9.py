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


    for i in range(len(word) - 5):
        if word[i] == word[i + 1] and word[i + 2] == word[i + 3] and word[i + 4] == word[i + 5]:
            return True
    return False


def find_three_consecutive_pairs():

    result = []

    with open('words.txt') as fin:
        for line in fin:
            word = line.strip()
            if has_three_consecutive_pairs(word):
                result.append(word)

    return result


def palindrome_odometer():
    for i in range(1, 6):
        if a[i] == word[i-1]:
            return True


def is_palindrome(x: int):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False



    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10


def get_four_digit_palindromes():
    result = []
    for first_two in range(10, 100):  # от 10 до 99

        palindrome = int(str(first_two) + str(first_two)[::-1])
        result.append(palindrome)
    return result


def get_five_digit_palindromes():
    result = []
    for first_two in range(10, 100):  # от 10 до 99
            for middle in range(0,10):
                palindrome = int(str(first_two) + str(middle) + str(first_two)[::-1])
                result.append(palindrome)
    return result

def get_for_plus_one_palindrome():
    result = []
    for x in get_four_digit_palindromes():
        z = x+1
        for begin in range(0,10):
            y = int(str(begin)+str(z))
            if y in get_five_digit_palindromes():
                result.append(y)
    return result
print(get_for_plus_one_palindrome())

def get_for_plus_one_plus_one_palindrome():
    result = []
    for x in get_for_plus_one_palindrome():
        z = x+1
        y = int(str(z)[:4])
        if y in get_four_digit_palindromes():
            result.append(y)
    return result

def puzzlers():
