def reverse_list(a):
    if len(a) == 1:
        return a[0]
    l = reverse_list(a[1:]).append(a[0])
    return l