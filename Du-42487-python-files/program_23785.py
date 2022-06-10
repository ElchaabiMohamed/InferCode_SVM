def reverse_list(l, n=None):
    if l == []:
        return n
    if n == None:
        return reverse_list(l[:-1], [l[-1]])
    return reverse_list(l[:-1], n + [l[-1]])
    
    
