def power(n,m):
    if m == 0:
        return 0
    elif n == 1:
        return 1
    return n + power(n-1)**m