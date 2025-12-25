n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

result = -1
left, right = 0, n - 1
step = 0
second_step_elements = []

while left <= right:
    mid = (left + right) // 2
    step += 1
    if step == 2:
        second_step_elements = arr[left:right + 1]

    if arr[mid] == k:
        result = mid
        break
    elif arr[mid] < k:
        left = mid + 1
    else:
        right = mid - 1

print(' '.join(map(str, second_step_elements)))
print(result)