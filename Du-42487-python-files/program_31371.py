def maximum(l, max_n=None):
    if not len(l):
        return max_n
    if not max_n or l[0] > max_n:
        return maximum(l[1:], l[0])
    return maximum(l[1:], max_n)
