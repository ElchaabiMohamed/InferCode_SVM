def reverse_list(l):
    if not l: 
        return l
    return l[-1:] + reverse_list(l[:-1]) 