def reverse_list(a):
    if len(a) == 1:
        return a
    l = reverse_list(a[1:])
    l.append(a[0])
    return l