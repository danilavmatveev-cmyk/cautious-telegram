def first(text):
    return text[0]
def last(text):
    return text[-1]
def middle(text):
    return text[1:-1]
def is_palindrome(text:str):
    if len(text) <= 1:
        return True
    elif first(text) == last(text):
        return is_palindrome(middle(text))
    else:
        return False
print(is_palindrome("forof"))
