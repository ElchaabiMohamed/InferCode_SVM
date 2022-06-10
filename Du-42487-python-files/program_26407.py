def selectionsort(l, o=None):
    if not o:
        o = []
        l = l[:]
    if not len(l):
        return o
    small = min(l)
    l.remove(small)
    o.append(small)
    return selectionsort(l, o)
