while True:
    tiles = input("Введите количество плиток ")
    if tiles.isdigit():
        tiles = int(tiles)
        if tiles % 2 == 0:
            if tiles == 0:
                print(" ")
            else:
                for i in range(tiles):
                    for j in range(tiles):
                        if (i+j) % 2 == 0:
                            print("■", end=" ")
                        else:
                            print("□", end=" ")
                    print()
        else:
            print("Ошибка,нужно ввести четное число!")
    else:
       print("Ошибка, нужно ввести целое число!")
       continue
    break
