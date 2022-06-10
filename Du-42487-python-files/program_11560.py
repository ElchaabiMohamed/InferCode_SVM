def fibonacci(s):
    if s == 0:
        return 0
    if s in (1,2):
        return 1
    return fibonacci(s-1) + fibonacci(s-2)
