import math
def hypotenuse(a,b):
    csquared = a ** 2 + b ** 2
    print('сумма квадратов равна: ', csquared)
    result = math.sqrt(csquared)
    print(f'Длина гипоттнузы равна: {result:.2f}')
    return result
hypotenuse(2,4)