def power(m,n):
    while n > 1:
        return m ** m + power( m , n -1)
