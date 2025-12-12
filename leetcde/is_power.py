def is_power(a,b):

    if a == 1:
        return True
    elif a % b != 0 or a < b:
        return False
    else:
        return is_power(a // b, b)

print (is_power(12,2))
