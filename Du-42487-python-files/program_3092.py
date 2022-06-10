def minimum(l):
    if len(l) == 1:
        return l[0]

    if l[-1] < l[0]:
        l.pop(0)
    else:
        l.pop()

    return minimum(l)