def minimum(a):

    if len(a) == 1:
        return a[0]

    if a[-2] > a[-1]:
        a[-2], a[-1] = a[-1], a[-2]
    a.pop()

    return minimum(a)
    