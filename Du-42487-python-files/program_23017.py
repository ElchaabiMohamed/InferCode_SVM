def reverse_list(n):
    if len(n) == 0:
        return []
    return [n[-1] + reverse_list(1[:-1])]
