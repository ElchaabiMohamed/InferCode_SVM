
def maximum(l):

    if len(l) == 1:
        return l[0]

    else:
        l = max(l[0], maximum(l[1:]))
        return l
