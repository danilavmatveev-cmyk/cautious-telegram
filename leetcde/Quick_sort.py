def sort_arr(lst):
    n = len(lst)
    if n < 2:
        return lst
    mid = n // 2
    if lst[mid] < lst[0] < lst[n - 1] or lst[n-1] < lst[0] < lst[mid]:
        pivot = lst[0]
    elif lst[0] < lst[mid] < lst[n - 1] or lst[n - 1] < lst[mid] < lst[0]:
        pivot = lst[mid]
    else:
        pivot = lst[n - 1]


    less = [i for i in lst if i< pivot]
    equal = [i for i in lst if i == pivot]
    greater = [i for i in lst if i > pivot]

    return sort_arr(less) + equal + sort_arr(greater)
print(sort_arr([1,34,56,7,3,9,888,4,3,6]))
