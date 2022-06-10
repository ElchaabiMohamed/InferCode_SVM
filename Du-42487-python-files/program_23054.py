def minimum(a):
    if a == []:
        return b[0]
    if a[-1] < a[-2]:
        b.append(a[-1])
        if len(b) > 1:
            if b[0] > b[1]:
                b.remove(b[0])
            else:
                b.remove(b[1])
    return minimum(a[:-1])