def power(m, n):
    if n == 1:
        return m
    else:
        return m * power(m, n-1)