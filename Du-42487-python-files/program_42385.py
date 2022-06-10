def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        maxi = minimum(l[1:])
        return l[0] if l[0] > maxi else maxi