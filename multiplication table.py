while True:
    number = input("Введите число ")
    if number.isdigit():
        number = int(number)
        if number == 0:
            print("0 x 0 = 0")
        else:
            for j in range(number+1):
                for i in range(number+1):
                    n = i * j
                    print(f"{j} x {i} = {n}")
                j =j+1
    else:
        print("Ошибка, нужно ввести целое число!")
        continue
    break


