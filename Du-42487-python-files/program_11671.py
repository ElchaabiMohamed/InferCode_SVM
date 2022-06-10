def minimum(a):
    if len(a) == 1:
        return a[0]

    small = a[0]

    if small < minimum(a[1:]):
        return small

    else:
        return minimum(a[1:])
