numbers = int(input())
seq_list = []

while numbers != 0:
    seq_list.append(numbers)
    numbers = int(input())

def seq_div_three(seq_list):
    new_list = []

    for i in range(len(seq_list)):

        if seq_list[i] % 3 == 0:
            new_list.append(seq_list[i])

    print(sum(new_list))

seq_div_three(seq_list)