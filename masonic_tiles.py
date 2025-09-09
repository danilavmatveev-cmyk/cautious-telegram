while True:
    tiles = input("Введите количество плиток ")
    if tiles.isdigit():
        tiles = int(tiles)
        if tiles == 0:
            print(" ")
        else:
            for i in range(tiles):
                for j in range(tiles):
                    print("■ □ ", end="")
                print()
    else:
        print("Ошибка, нужно ввести целое число!")
        continue
    break
