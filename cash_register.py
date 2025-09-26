quantity = input("Введите количество товаров: ")
while True:
    if quantity.isdigit():
        quantity = int(quantity)
        total = 0
        for i in range(quantity):
            price = input(f"Введите цену товара {i+1}: ")
            while True:
                if price.isdigit():
                    price = int(price)
                    total  += price
                    break
                else:
                    print("Ошибка: введите число для количества!")

        print(f"Общая сумма: {total}")

        if total >= 500:
            discount = 0
            discount_text = "нет"
            total_amount = total
        elif total % 13 == 0 or total % 101 == 0:
            discount = 31
            discount_text = "31 %"
            total_amount = total * 0.69
        else:
            discount = 5
            discount_text = "5%"
            total_amount = total * 0.95

        print(f"Скидка: {discount_text}")
        print(f"Итоговая сумма: {total_amount:.2f}")
        print(f"Количество товаров: {quantity}")
        average_price = total_amount / quantity
        print(f"Средняя цена: {average_price:.2f}")
        break

    else:
        print("Ошибка: введите число для количества!")
        quantity = input("Введите количество товаров: ")




