numbers = int(input())
sequence_list = []
for i in range (numbers):
    sequence  = int(input())
    sequence_list.append(sequence)

sum_sequence = 0
for j in range(len(sequence_list)):
    if sequence_list [j] % 6 == 0 and sequence_list [j] % 10 == 4:
        sum_sequence += 1
    else:
        sum_sequence += 0
print(sum_sequence)
