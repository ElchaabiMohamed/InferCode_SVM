def reverse_list(l, r=None):
    if not r:
        r = []
    if not l:
        return r
    r.append(l.pop())
    return reverse_list(l, r)
