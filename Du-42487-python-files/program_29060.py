def reverse_list(l):
    return l[-1] + reverse_list(l[:-1])
