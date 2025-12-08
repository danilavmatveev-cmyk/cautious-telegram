def check_fermat(a,b,c,n):
   if n>2:
        if a**n+b**n == c**n:
            print('«Не может быть, Ферма ошибся!»')
        else:
            print("Нет, это не работает")
   else:
        print('введите значение степени больше 2')
check_fermat(5,6,7,1)