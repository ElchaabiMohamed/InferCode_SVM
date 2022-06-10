def sumup(n):
    if not n:
        return n
    if n == 1:
        return 1
    return n + sum(n-1)