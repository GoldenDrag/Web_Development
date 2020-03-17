import math

x = int(input())
cnt = 0

for i in range(1, int(math.sqrt(x))):
    if x % i == 0:
        cnt = cnt + 1
cnt = cnt * 2

if(x % math.sqrt(x) == 0):
    cnt = cnt + 1

print(cnt)