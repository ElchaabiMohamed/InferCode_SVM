def reverse_list(a):
    if len(a) == 0:
        return []

    k = a[-1]
    a.pop()
    return [k] + reverse_list(a)