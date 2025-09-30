def guess_code(password: str):

    password_list = list(password)
    attempts = 0

    for j in range(1,11):
        code = input("")
        code_list = list(code)
        if len(code_list) != 5:
            print("Ошибка! Нужно ввести ровно 5 цифр")
            continue

        attempts += 1




        if code_list == password_list:
            print(f"Угадано цифр: 5")
            print(f"На своих местах: 5" + "\n")
            print(f"Поздравляем! Вы угадали пароль {password} за {attempts} попыток!")
            break

        number = 0
        for i in range(len(password_list)):
            if code_list[i] in password_list:
                number = number + 1
            else:
                number = number + 0

        place_number = 0
        for n in range(len(code_list)):
            if password_list[n] == code_list[n]:
                place_number = place_number + 1
            else:
                place_number = place_number + 0


        print(f"Угадано цифр: {number}")
        print(f"На своих местах: {place_number}")

        if j < 10:
            print("Неверно, попробуйте ещё раз")




    else:
        print("Игра окончена! Правильный пароль был: 39412")


















guess_code("39412")


