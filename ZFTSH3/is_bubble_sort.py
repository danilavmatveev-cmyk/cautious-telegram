n = int(input())
A = n*[0]
for i in range (n):
    A[i] = int(input())
for i in range(3):
    for j in range(0, len(A) - 1-i):
        if A[j] >= A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print(*A)
