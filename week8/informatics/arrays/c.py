n = int(input())
s = list(map(int, input().split(" ")))
cnt = 0

for i in range(n):
    if s[i] > 0:
        cnt += 1 
print(cnt)       