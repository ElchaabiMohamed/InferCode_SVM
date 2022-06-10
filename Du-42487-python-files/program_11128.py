def minimum(l):
    if len(l) == 1:
        return l[0]
    else:
        min_a, min_b = l[0], minimum(l[1:])
        if min_a > min_b:
            min_a = min_b
        return min_a
