def sumup(n):
    if n == 0:
        return 1

    return n + sumup(n-1)