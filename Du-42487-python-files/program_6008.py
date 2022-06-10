
def power(n,n2):
    if n == 0:
        return 1
    return n2 * power(n-1,n2)