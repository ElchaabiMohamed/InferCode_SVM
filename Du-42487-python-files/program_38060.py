def minimum(l):
    l = sorted(l)
    if len(l) == 1:
        return l[0]
    l.pop()
    return minimum(l)