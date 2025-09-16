number = input("Введите число: ")
try:
   number = int(number)

   fib_list =[]
   a = 0
   b = 1
   for i in range(number):
     fib_list.append(a)
     c = a
     a = b
     b = c + b
   print(fib_list)

except ValueError:
    print("Ошибка! Введите корректное число!")



