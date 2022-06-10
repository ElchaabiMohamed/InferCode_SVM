def power(m , n):
    if n == 0 or m == 1:
        return 1

    return m * power(m , n - 1)