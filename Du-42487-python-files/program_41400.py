def minimum(l):
    if not l or len(l) == 1:
        return l
    tail_min = minimum(l[1:])
    return l[0] if l[0] < tail_min else tail_min
    
    
