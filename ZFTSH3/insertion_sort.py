n = int(input())
A = n*[0]
for i in range (n):
    A[i] = int(input())
for i in range(2):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] < key:
        A[j], A[j + 1] = A[j + 1], A[j]
        j = j - 1
print(*A)