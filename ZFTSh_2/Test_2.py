def hanoi_towers(n, from_rod, to_rod, aux_rod):

    if n == 0:
        return  ""

    if n == 1:

        return  f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}"

print(hanoi_towers(1, "A", "C", "D"))