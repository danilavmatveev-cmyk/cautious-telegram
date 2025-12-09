def is_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def input_is_triangle():
    try:
        a = int(input("Введите a:"))
        b = int(input("Введите b:"))
        c = int(input("Введите c:"))

        result = is_triangle(a, b, c)
        print(result)
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа")


if __name__ == "__main__":
    input_is_triangle()