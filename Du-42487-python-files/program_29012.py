def power(x, y):
    if y == 0:
        return x

    return power(x**y, y - 1)



