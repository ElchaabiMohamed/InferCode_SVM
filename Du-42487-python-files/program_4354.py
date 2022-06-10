def fibonacci(n):
    if n == (0 or 1):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)