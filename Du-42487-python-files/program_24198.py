def fibonacci(n, l=0, c=1):
    if not n:
        return c
    return fibonacci(n-1, c, l+c)
