def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return n * factorial(n - 1)
