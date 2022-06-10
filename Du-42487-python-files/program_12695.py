def power(i, n):
    if n == 0:
        return 1
    else:
        return i * power(i, n-1)

print((power(2, 3)))