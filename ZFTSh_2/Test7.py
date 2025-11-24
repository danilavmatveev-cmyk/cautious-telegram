def summa_ind(seq):
    if not seq:
        return 0
    sub_summa = summa_ind(seq[1:])
    return sub_summa + 1

print(summa_ind([1,2,10,4,5]))
