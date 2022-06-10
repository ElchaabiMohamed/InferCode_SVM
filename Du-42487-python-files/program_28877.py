def minimum(l, m=None):
    if not len(l):
        return m
    if not m or l[0] < m:
        return minimum(l[1:], l[0])
    return minimum(l[1:], m)
