def reverse_list(a,b=[]):
    if len(b) != len(a) and len(a) != 0:
        b.append(a[-1])
        return reverse_list(a[:-1], b)
    else:
        return b