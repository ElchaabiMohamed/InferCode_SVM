def fibonacci(a, prev = 0, curr =1):
    if a == 0:
        return 0
    prev = curr
    return 1 + fibonacci(a - 1, prev, curr)