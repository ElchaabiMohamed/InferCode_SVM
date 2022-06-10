
def reverse_list(l):

    if len(l) == 1:
        return l

    else:
        j = l.pop(0)
        return reverse_list(l).append(j)