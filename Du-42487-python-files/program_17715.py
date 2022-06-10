def maximum(n):
    if len(n) == 1:
        return n[0]
    else:
        min_ret = maximum(n[1:])
        return n[0] if n[0] > min_ret else min_ret