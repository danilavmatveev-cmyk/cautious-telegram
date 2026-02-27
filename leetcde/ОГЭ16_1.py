N = int(input())
count = 0
speed_ov = 0
for i in range (N):
    speed = int(input())
    if speed <= 40:
        count += 1
    speed_ov = speed_ov+speed
speed_av = round(speed_ov/N,1)
print(speed_av)
if count < 2:
    print('NO')
else:
    print('YES')
