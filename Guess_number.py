def bin_search(random_number:int):
    while True:
        number = int(input(""))
        if number < random_number:
            print(f"Неверно! Число больше {number}")
        elif number > random_number:
            print(f"Неверно! Число меньше {number}")
        else:
            print("Верно!")
            break



bin_search(0)










