def minimum(a):
    if len(a) == 1:
        return a[0]
    if a[0] < a[1]:
        a.append(a[0])
    return minimum(a[1:])