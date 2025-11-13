def hanoi_towers(n, from_rod, to_rod, aux_rod):

    if n == 0:
        return

    if n == 1:
        print(f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}")
        return

    hanoi_towers(n - 1, from_rod, aux_rod, to_rod)
    print(f"Переместить диск {n} со стержня {from_rod} на стержень {to_rod}")
    hanoi_towers(n - 1, aux_rod, to_rod, from_rod)






hanoi_towers(3, 'A', 'C', 'B')