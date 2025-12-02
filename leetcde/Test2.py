def do_twice (f,value):
    f(value)
    f(value)
def print_twice(value1):
    print(value1)
    print(value1)
def do_four(f,value):
    do_twice(f, value)
    do_twice(f, value)
do_four(print_twice,"спам")