
def minimum(l):

    if len(l) == 1:
        return l[0]

    else:
        l = min(l[0], mininum(l[1:]))
        return l
