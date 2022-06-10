
def reverse_list(l):

    if len(l) == 1:
        return l

    else:
        return list(l.pop(0)) + reverse_list(l)