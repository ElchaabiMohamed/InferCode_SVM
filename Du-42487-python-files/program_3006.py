
def fibonacci(n):
    
    if n == 0 or n == 1:
        return 1
    return n * fibonacci(n-1) + fibonnaci(n-2)