def sumup(n):
    n = int(n)
    if n > 0:
        n = n + sumup(n-1)
        return n
    else:
        print(n)
