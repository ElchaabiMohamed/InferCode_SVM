def fibonacci(s):
    if s in (0,1):
        return 1
    return fibonacci(s-1) + fibonacci(s-2)
