cache = {}
def hanoi_towers(n, from_rod, to_rod, aux_rod):

    if (n, from_rod, to_rod, aux_rod) in cache:
        return cache[n, from_rod, to_rod, aux_rod]

    if n == 0:
        return  ""

    if n == 1:
        result = f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}\n"
        cache[(n, from_rod, to_rod, aux_rod)] = result
        return result



    step1 = hanoi_towers(n - 1, from_rod, aux_rod, to_rod)
    step2 = f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}\n"
    step3 = hanoi_towers(n - 1, aux_rod, to_rod, from_rod)
    result = step1+step2+step3
    cache [(n, from_rod, to_rod, aux_rod)] = result
    return result





print(hanoi_towers(3, "A", "C", "B"))