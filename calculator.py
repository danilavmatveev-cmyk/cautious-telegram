import sys
number_list = []
operator_list = []
symbol = ""
while symbol != "=":
    number = float(input("Число: "))
    number_list.append(number)

    symbol = input("Оператор (+,-,*,/,^) или =: ")
    if symbol == "=":
        break
    else:
        operator_list.append(symbol)
        continue

result = number_list [0]
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
            sys.exit()
        result /= next_number

    else:
        result **= next_number

print(result)





