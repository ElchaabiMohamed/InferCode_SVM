def maximum(a):
    if len(a) == 1:
        return a[0]

    big = a[0]

    if big > maximum(a[1:]):
        return big

    else:
        return maximum(a[1:])
