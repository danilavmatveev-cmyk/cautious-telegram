def check_fermat(a,b,c,n):

   if n>2:
        if a**n+b**n == c**n:
            print('«Не может быть, Ферма ошибся!»')
        else:
            print("Нет, это не работает")
   else:
        print('введите значение степени больше 2')


def input_fermat():
    try:
        a = int(input ("Введите a:" ))
        b = int(input ("Введите b:" ))
        c = int(input ("Введите c:" ))
        n = int(input ("Введите степень:"))
        check_fermat(a, b, c, n)
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа")

if __name__ == "__main__":
    input_fermat()