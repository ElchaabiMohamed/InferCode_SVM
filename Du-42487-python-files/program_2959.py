def power(m, n):
    if not n:
        return 1
    return m * power(m, n-1)
