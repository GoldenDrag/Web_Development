def pow(a, n):
    return a**n

if __name__== "__main__":
    a, n = input().split()
    print(pow(int(a), int(n)))