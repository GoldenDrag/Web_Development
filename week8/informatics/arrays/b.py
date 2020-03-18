x = int(input())
# arr = []

print(*(x for x in input().split() if not int(x) % 2))