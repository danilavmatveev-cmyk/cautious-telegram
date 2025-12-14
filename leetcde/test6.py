def first(text):
    return text[0]
def last(text):
    return text[-1]
def middle(text):
    return text[1:-1]
def is_txet(text:str):
    if len(text) <= 1:
        return text
    return last(text) + is_txet(middle(text)) + first(text)
print(is_txet("rwsdsdfewfv dfdf"))