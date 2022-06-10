def reverse_list(l):
    if len(l) == 1 or not l:
        return l
    return [l[-1]] + reverse_list(l[:-1])
