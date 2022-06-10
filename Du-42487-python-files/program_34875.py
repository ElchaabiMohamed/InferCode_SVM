def reverse_list(n):
    if not n:
        return []
    return [n.pop()] + reverse_list(n)
