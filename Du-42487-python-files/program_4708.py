def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        nl = maximum(l[1:])
    if l[0] > nl:
        return l[0]
    else:
        return  nl