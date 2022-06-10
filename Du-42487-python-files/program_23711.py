
def power(n, p):

    if p == 0:
        return 1

    if p == 1:
        return n

    else:
        return n * power(n, (p - 1))
