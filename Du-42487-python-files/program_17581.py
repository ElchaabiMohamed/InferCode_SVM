def power(m, n):
    if n == 0:
        return 1
    print((m *power(m,n-1)))
    return m * power(m, n-1)