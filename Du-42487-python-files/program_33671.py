def reverse_list(l, ding=None):
    if not ding:
        ding = []
    if not l:
        return ding
    ding.append(l.pop())
    return reverse_list(l, ding)