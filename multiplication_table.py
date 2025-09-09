number1 = input("Введите первое число: ")
symbol = input("Введите символ операции: ")
number2 = input("Введите второе число: ")
n1 = abs(number1)
n2 = abs(number2)
if n1.isdigit() and n2.isdigit():
    number1 = float(number1)
    number2 = float(number2)
    if symbol == "*":
        result = number1*number2
    elif symbol == "/":
        if number2 == 0:
            print ("Деление на 0 запрещено!")
        else:
            result = number1 / number2
    elif symbol == "+":
        result = number1 + number2
    elif symbol == "-":
        result = number1 - number2
        print(f"{result}")
    else:
        print("Ошибка!")
