import math
def mysqrt(a, epsilon=1e-10):

    if a < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен")
    if a == 0:
        return 0
    if a == 1:
        return 1


    x = a / 2

    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    return y
def test_square_root(a):
    diff = abs(mysqrt(a)- math.sqrt(a))
    print("a     mysqrt(a)           math.sqrt(a)         diff")
    print("-     ---------           ------------         ----")
    print(f"{float(a):<3}    {mysqrt(a):<16.15}  {math.sqrt(a):<16.15}  {diff}")

test_square_root(25)