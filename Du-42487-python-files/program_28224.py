def reverse_list(a):
    if len(a) == 1:
        return a
    return a[0].append(reverse_list(a[1:]))