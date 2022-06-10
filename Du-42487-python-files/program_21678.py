def power(m,n):
    if n == 1:
        return 0
    return m * m + power( m , n -1)
