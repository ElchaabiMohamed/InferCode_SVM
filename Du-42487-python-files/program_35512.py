def sumup(n):
    if n > 0:
        n = n + sumup(n-1)
    else:
        print(n)
