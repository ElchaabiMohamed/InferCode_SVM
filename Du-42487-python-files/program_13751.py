def minimum(l):
    if not l:
        return l
    if len(l) == 1:
        return l[0]
    tail_min = minimum(l[1:])
    if tail_min == []:
        return l[0]
    return l[0] if l[0] < tail_min else tail_min
    
    
