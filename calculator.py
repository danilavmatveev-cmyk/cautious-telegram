
number_list = []
operator_list = []
symbol = ""
while symbol != "=":
    try:

        number = float(input("Введите число: "))
        number_list.append(number)

        symbol = input("Введите оператор (+,-,*,/,^) или =: ")

        if symbol == "=":
            break
        elif symbol in ["+", "-", "*", "/","^"]:
            operator_list.append(symbol)
        else:
            print("Ошибка! Неверный оператор. Попробуйте снова.")
            continue

    except ValueError:
        print("Ошибка! Введите корректное число.")
        continue

result = number_list[0]
for i in range(len(operator_list)):
    next_number = number_list[i + 1]


    if operator_list[i] == '+':
        result += next_number
    elif operator_list[i] == '-':
        result -= next_number
    elif operator_list[i] == '*':
        result *= next_number
    elif operator_list[i] == '/':
        if next_number == 0:
            print("Ошибка: деление на ноль!")
            result = "не определено"
            break
        result /= next_number
    elif operator_list[i] == '^':
        result **= next_number

print(f"Результат: {result}")





