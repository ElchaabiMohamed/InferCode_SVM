def minimum(l, c=None):
    if c == None:
        return minimum(l[1:], l[0])
    if l == []:
        return c
    if l[0] > c:
        return minimum(l[1:], l[0])
    else:
        return minimum(l[1:], c)
