def reverse_list(n):
    if len(n) == 0:
        return 0
    return reverse_list(n.reverse())
