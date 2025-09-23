n1 = input("ведите первое число: ")
n2 = input("введите второе число: ")
N = input ("введите количество чисел в последовательности: ")
a = 0
try:
   n1 = int(n1)
   n2 = int(n2)
   N = int(N)

   seq_list = [n1,n2]
   for i in range(N-2):
     a = n1 + n2 + n1*n2
     seq_list.append(a)
     n1 = n2
     n2 = a
     
   print(seq_list)

except ValueError:
    print("Ошибка! Введите корректное число!")
