def fibonacci(a, prev = 1, curr =1):
    if a == 0:
        return prev
    tmp = curr
    curr += prev
    prev = curr
    return prev + fibonacci(a - 1, prev, curr)