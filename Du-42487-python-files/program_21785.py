def minimum(l):
    if len(l) == 1:
        return l[0]
    tail_min = minimum(l[1:])
    return l[0] if l[0] < tail_min else tail_min
    # Could do this but ought not use min I suppose...
    # return min(l[0], rmin(l[1:]))
