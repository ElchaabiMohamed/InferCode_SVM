def maximum(l):
    l = sorted(l, reverse=True)
    if len(l) == 1:
        return l[0]
    l.pop()
    return maximum(l)