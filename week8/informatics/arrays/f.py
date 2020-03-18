n = int(input())
s = list(map(int, input().split(" ")))
cnt = 0
for i in range(n):
    if i - 1 < 0:
        continue
    if i + 1 > n:
        continue
    if s[i+1] < s[i] > s[i-1]:
        cnt += 1 
print(cnt)       