def minimum(l):
    if len(l) == 1:
        return l[0]

    m = minimum(l[1:])

    return m if m < l[0] else l[0]
