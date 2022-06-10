def reverse_list(n):
    if n == []:
        return 0
    return reverse_list(n.reverse())
