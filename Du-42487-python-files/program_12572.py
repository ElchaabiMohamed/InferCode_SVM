def maximum(l):
    if len(l) == 1:
        return l[0]
    tail_max = maximum(l[1:])
    return l[0] if l[0] > tail_max else tail_max
    # Could do this but ought not use max I suppose...
    # return max(l[0], maximum(l[1:]))
