def reverse_list(l):
    if len(l) == 1:
        return l
    return [l[-1]].extend(reverse_list(l[:-1]))
