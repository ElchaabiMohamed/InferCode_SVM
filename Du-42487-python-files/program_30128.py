def fibonacci(n, older=0, old=1):
    if n == 0:
        return old
    return fibonacci(n-1, old, older+old)
