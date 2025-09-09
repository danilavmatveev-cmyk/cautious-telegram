quantity = input("Введите количество товаров: ")
while True:
    if quantity.isdigit():
        quantity = int(quantity)
        total = 0
        for i in range(quantity):
            price = input(f"Введите цену товара {i+1}: ")
            if price.isdigit():
                price = int(price)
                total  += price
            else:
                print("Ощибка: Введите число для цены!")
        print(f"Общая сумма: {total}")
        break
    else:
        print("Ошибка: введите число для количества!")
        quantity = input("Введите количество товаров: ")
    