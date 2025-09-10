import random

random_number = random.randint(0, 100)

def bin_search(random_number:int):
    number = int(input(" "))

    while number != random_number:
        if number < random_number:
            print(f"Неверно! Число больше {number}")
        elif number > random_number:
            print(f"Неверно! Число меньше {number}")

        try:
            number = int(input(" "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue

    print("Верно!")



bin_search(50)










