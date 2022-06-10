def sumup(n):
    if int(n) == 0:
        return '0'
    
    return n + sumup(n-1)
    
