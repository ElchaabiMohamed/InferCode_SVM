def fibonacci(a, prev = 0, curr =1):
    if a == 0:
        return prev
    prev = curr
    return prev + fibonacci(a - 1, prev, curr)