def xor(a, n):
    if a + n == 1:
        return 1
    else:
        return 0

if __name__== "__main__":
    a, n = input().split()
    print(xor(int(a), int(n)))