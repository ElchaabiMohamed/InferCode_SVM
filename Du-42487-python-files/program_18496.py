def minimum(l):
    if len(l) == 1:
       return l[0]

    else:
       return min(l[0], findMinimum(l[1:]))