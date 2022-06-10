
def reverse_list(l):

    if len(l) == 1:
        return l

    else:
        j = list(l.pop(0))
        return reverse_list(l) + j