def minimum(l):
    if len(l)==1:
        return l[0]
    else:
        m1 = minimum(l[0:len(l) / 2])
        m2 = minimum(l[len(l) / 2:])
        if m1 < m2:
            return m1
        else:
            return m2