def minimum(n):
    if len(n) == 1:
        return n[0]
    else:
        minr = minimum(n[1:])
        return n[0] if n[0] < minr else minr
