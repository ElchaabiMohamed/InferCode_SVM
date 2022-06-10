def maximum(l):
    if len(l)==1:
        return l[0]
    else:
        m1 = maximum(l[:len(l) // 2])
        m2 = maximum(l[len(l) // 2:])
        if m1 > m2:
            return m1
        else:
            return m2