
def reverse_list(l):

    if len(l) == 0:
        return []

    else:
        return reverse_list(l[1:]).append(l.pop(0))