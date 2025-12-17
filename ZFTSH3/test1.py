n = int(input())
A = n*[0]
for i in range (n):
    A[i] = int(input())

B = sorted(A, reverse=True, key = lambda x: x**2 - 2*x)
print(*B)