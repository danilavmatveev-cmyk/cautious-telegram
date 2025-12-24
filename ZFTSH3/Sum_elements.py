
A = []
n, m = map(int, input().split())
for i in range(n):
    A.append(list( map(int, input().split())))

sum_element = 0

for i in range(n):
    for j in range(m):
        sum_element += A[i][j]
print(sum_element)