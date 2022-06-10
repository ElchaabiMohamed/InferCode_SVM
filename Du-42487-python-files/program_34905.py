def factorial(n):
    if n == 0: # base case : no more calls to factorial()
        return 1
    return n * factorial(n-1)
