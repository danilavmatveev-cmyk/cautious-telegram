number = input("Введите число: ")
number_str = number.replace(' ', '')
reversed_number_str = number_str[::-1]

try:
    number_float = float(number_str)
    if number_str  == reversed_number_str:
        print("Число палиндром")
    else:
        print("Число не палиндром")
except ValueError:
    print("Ошибка! Введите корректное число!")



