def power(x, y):
    if y == 1:
        return x
    return x * power(x, y - 1)
