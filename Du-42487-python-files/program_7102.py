def maximum(l, c=None):
    if c == None:
        return maximum(l[1:], l[0])
    if l == []:
        return c
    if l[0] > c:
        return maximum(l[1:], l[0])
    else:
        return maximum(l[1:], c)
