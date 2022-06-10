def power(m, n):
    if n == 0:
        return 1
    print((m, n))
    return m * power(m, n-1)