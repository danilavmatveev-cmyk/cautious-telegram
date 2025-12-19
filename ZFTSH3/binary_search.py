def binary_search(A, k):

    left = 0
    right = len(A)-1
    step = 0

    while right >= left:
        step += 1

        if step == 2:
            elements = []
            for i in range(left, right + 1):
                elements.append(str(A[i]))

            print(" ".join(elements))

        mid = (left + right) // 2

        if A[mid] == k:
            return mid

        if A[mid] > k:
          right = mid-1

        else:
          left = mid + 1
    return -1

n = int(input())
k = int(input())
A = n*[0]
for i in range (n):
    A[i] = int(input())

A.sort()

print(binary_search(A,k))