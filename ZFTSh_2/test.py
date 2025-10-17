cache = {}
def hanoi_towers(n, from_rod, to_rod, aux_rod):



    if n == 0:
        return  ""

    if n == 1:
        cache [(n, from_rod, to_rod, aux_rod)] = hanoi_towers(0,0,1,0)
        print(f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}")
        return cache [(n, from_rod, to_rod, aux_rod)]

    if n == 2:
        cache [(n, from_rod, to_rod, aux_rod)] = (hanoi_towers(n, n-1, 0, 1) + hanoi_towers(n, n-2, 1, 1)
                                                  + hanoi_towers(n, n-2, 2, 0))
        return cache [(n, from_rod, to_rod, aux_rod)]

    if n == 3:
        cache [(n, from_rod, to_rod, aux_rod)] = (hanoi_towers(n, n-1, 0, 1) and hanoi_towers(n, n-2, 1, 1)
                                                  and hanoi_towers(n, n-2, 2, 0))
        return cache [(n, from_rod, to_rod, aux_rod)]




print(hanoi_towers(2, "A", "C", "D"))