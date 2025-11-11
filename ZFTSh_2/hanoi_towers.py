def hanoi_towers(n, from_rod, to_rod, aux_rod):

    if n == 0:
        return  ""

    if n == 1:
        result = f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}\n"
        return result

    step1 = hanoi_towers(n - 1, from_rod, aux_rod, to_rod)
    step2 = f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}\n"
    step3 = hanoi_towers(n - 1, aux_rod, to_rod, from_rod)
    result = step1+step2+step3
    return result





print(hanoi_towers(4, '1', '3', '2'))