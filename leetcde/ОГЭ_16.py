N = int(input())
count = 0
arr = []
for i in range (N):
    arr.append(int(input()))
vel_mid = round(sum(arr)/N,1)
print(vel_mid)

for i in range(N):
    if arr[i] <= 40:
        count += 1

if count < 2:
    print('NO')
else:
    print('YES')

