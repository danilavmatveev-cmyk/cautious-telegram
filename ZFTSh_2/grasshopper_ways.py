cache = {}
def grasshopper_ways (n):
    if n in cache:
        return cache[n]

    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    result = grasshopper_ways(n-1) + grasshopper_ways(n-2)
    cache[n] = result
    return result
print(grasshopper_ways (1))