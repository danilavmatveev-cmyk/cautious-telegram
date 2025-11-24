def summa(list):
    if list == []:
        return 0
    sub_summa = summa(list[1:])
    return list[0] + sub_summa

print(summa([1,2,10,4,5]))
