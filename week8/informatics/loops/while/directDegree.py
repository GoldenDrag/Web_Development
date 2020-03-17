n = int(input())
i = 1
yes = False

while i <= n:
    if i == n:
        print('YES')
        yes = True
    i *= 2
if yes == False:
    print('NO')