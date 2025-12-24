A = []
n, m,s = map(int, input().split())
for i in range(n):
    A.append(list( map(int, input().split())))


for i in range(s):
    for j in range(m):
        print(A[i][j], end = '\t')
    print()