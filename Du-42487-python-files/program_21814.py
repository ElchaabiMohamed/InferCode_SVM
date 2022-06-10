def factorial(n):
    if int(n) == 1:
        return 1
    elif int(n) == 0:
        return 1
    return n * factorial(n-1)
    
