def power(n,p):
    if p == 0:
        return 1
    if p == 1:
        return n + 1
    return n ** p-1