def reverse_list(l):
    if not l:
        return []
    return [l.pop()] + reverse_list(l)
