
def sumup(n):
    print (n)

    if n == 0:
        return 1

    else:
        return n * sumup(n - 1)
