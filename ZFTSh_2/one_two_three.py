cache = {}

def one_two_three(current, target):

    if (current, target) in cache:
        return cache[(current, target)]

    if current == target:
        return 1
    if current > target:
        return 0
    if current == 33:
        return 0

    cache[(current, target)] = (one_two_three(current + 1, target) +
              one_two_three(current * 2, target) +
              one_two_three(current * 3, target))

    return cache[(current, target)]

total = one_two_three(3,15) * one_two_three(15,50)

print(total)
