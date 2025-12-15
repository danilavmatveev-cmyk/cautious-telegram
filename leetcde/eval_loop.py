import math
def eval_loop():
    result = None

    while True:
        line = input('> ')


        if line == 'готово':
            break
        result = eval(line)

    print(result)


eval_loop()