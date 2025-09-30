def guess_code(pasword: str):

    pasword_list = list(pasword)


    for j in range(9):
        code = input("")
        code_list = list(code)
        number = 0
        place_number = 0
        if len(code_list) == 5:
            if code_list != pasword_list:
                for i in range(len(pasword_list)):
                    if code_list[i] in pasword_list:
                       number = number + 1
                    else:
                        number = number + 0


                for n in range(len(code_list)):
                    if pasword_list[n] == code_list[n]:
                        place_number = place_number + 1
                    else:
                        place_number = place_number + 0

                print(f"Угадано цифр: {number}")
                print(f"На своих местах: {place_number}")
                print("Неверно, попробуйте ещё раз")
            else:
                print(f"Поздравляем! Вы угадали пароль {pasword} за {j} попыток!")
                break
        else:
            print("Ошибка! Нужно ввести ровно 5 цифр")

guess_code("39412")


