
def reverse_list(l):

    if len(l) == 0:
        return []

    else:
        l = reverse_list(l[1:]) + list(l.pop(0))
        return l