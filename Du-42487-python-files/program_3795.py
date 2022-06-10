def power(m,n):
    if n == 1:
        return m
    return m * m + power( m , n -1)
