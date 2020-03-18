n = int(input())
s = list(map(int, input().split(" ")))

for i in range(int(n/2)):
    temp = s[i]
    s[i] = s[n-i-1]
    s[n-i-1] = temp

print (" ".join(map(str, s)))