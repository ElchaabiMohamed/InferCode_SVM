def maximum(l):
    if not l:
        return l
    if len(l) == 1:
        return l[0]
    tail_max = maximum(l[1:])
    if tail_max == []:
        return l[0]
    return l[0] if l[0] > tail_max else tail_max
    
    
