def fibonacci(a, curr = 1):
    if a == 0:
        return curr
    return curr + fibonacci(a - 1, curr)