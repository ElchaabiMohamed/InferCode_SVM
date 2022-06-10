def reverse_list(a):
    if len(a) == 1 or len(a) == 0:
        return a
    return [a[-1]] + (reverse_list[:-1])