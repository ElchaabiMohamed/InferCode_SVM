def reverse_list(a,b=[]):
    if len(b) != len(a):
        b.append(a[-1])
        return reverse_list(a[:-1], b)
    else:
        return b