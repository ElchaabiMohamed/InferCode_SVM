def sumup(n):
    if int(n) == 0:
        return 0
    return int(n) + sumup(int(n)-1)
    
