cache = {}

def is_prime(n):
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = False
        return False
    if n == 2:
        cache[n] = True
        return True
    for i in range(2,n):
        if n % i == 0:
            cache[n] = False
            return False

    cache[n]= True
    return True


print(is_prime(911))