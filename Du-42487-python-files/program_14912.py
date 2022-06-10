def reverse(l):
    if not l: 
        return l
    return l[-1:] + reverse(l[:-1]) 