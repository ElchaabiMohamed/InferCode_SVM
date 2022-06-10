
def reverse_list(l):

    if len(l) == 1:
        return l

    else:
        return reverse_list(l[1:]).append(l.pop(0))