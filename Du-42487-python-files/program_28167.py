def power(m, n):
    if n == 0:
        return 1

    return (m * power(n-1))