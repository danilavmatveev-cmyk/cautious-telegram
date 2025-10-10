cache ={}
def one_two_three(current, target,cache):
    if (current,target) in cache:
        return cache[(current,target)]
    if current == target:
        return 1
    if current > target:
        return 0
    if current == 33:
            return 0
    result = (one_two_three(current + 1, target,cache) + one_two_three(current * 2, target,cache) + one_two_three(current * 3,target,cache))

    cache[(current,target)] = result
    return result




print(one_two_three(2, 50))