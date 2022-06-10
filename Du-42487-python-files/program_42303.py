def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        max_a, max_b = l[0], maximum(l[1:])
        if max_a < max_b:
            max_a = max_b
        return max_a
