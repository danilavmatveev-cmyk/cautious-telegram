def seq_div_three(*args):
    new_list = []

    for i in range(len(args)):

        if args[i] % 3 == 0:
            new_list.append(args[i])

    print(sum(new_list))

seq_div_three(1, 2, 4, 5, 7, 8, 0)