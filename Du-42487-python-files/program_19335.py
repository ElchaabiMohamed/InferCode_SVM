def reverse_list(a, b = []):
    if a == []:
        tmp = b
        b = []
        return tmp
    b.append(a[-1])
    return reverse_list(a[:-1], b)