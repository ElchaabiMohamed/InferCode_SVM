def maximum(l):
    if len(l) == 1:
        return l[0]
    return maximum(l[1:] if l[0] < l[-1] else l[:-1] )