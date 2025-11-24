def summa_ind(list):
    if not list:
        return 0
    sub_summa = summa_ind(list[1:])
    return sub_summa + 1

print(summa_ind([1,2,10,4,5]))
