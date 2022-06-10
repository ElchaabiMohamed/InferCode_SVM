def fibonacci(n, last=0, curr=1):
    if not n:
        return curr
    return fibonacci(n-1, curr, last + curr)
