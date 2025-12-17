def any_lowercase2(s):
    for c in s:
        if c.islower():
            return True

    return False
print(any_lowercase2("SС"))

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print(any_lowercase4("sc"))




def rotate_word(text:str,number):
    result_chars = []
    for char in text:
        if 'a' <= char <= 'z':
            
            shifted = chr((ord(char) - ord('a') + number) % 26 + ord('a'))
            result_chars.append(shifted)
        elif 'A' <= char <= 'Z':

            shifted = chr((ord(char) - ord('A') + number) % 26 + ord('A'))
            result_chars.append(shifted)
        else:

            result_chars.append(char)

    return "".join(result_chars)

print(rotate_word("rambler",10))