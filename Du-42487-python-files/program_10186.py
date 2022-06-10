def maximum(m):
    if len(m)==1:
        return m[0]
    else:
        a = m.pop()
        b = m.pop()
        if (a > b):
            m.append(a)
        else:
            m.append(b)
        return maximum(m)
