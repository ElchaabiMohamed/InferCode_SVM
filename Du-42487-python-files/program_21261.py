def sumup(n):
    if n == 1:
        return n

    return n + sumup(n-1)
