import sys
A = []
n, m, k = map(int, input().split())
for i in range(n):
    A.append(list( map(int, input().split())))



for i in range(n):
    for j in range(m):
       if A[i][j] == k:
           print(i+1,j+1)
           sys.exit()

print(-1, -1)

def find_position(matrix, k):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == k:
                return i + 1, j + 1
    return -1, -1

# Использование:
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(*find_position(A, k))
