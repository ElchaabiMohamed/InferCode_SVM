def reverse_list(a, reverse=None):
    if not reverse:
        reverse = []
    if len(a) < 1:
        return reverse
    reverse.append(a.pop())
    return reverse_list(a, reverse)
