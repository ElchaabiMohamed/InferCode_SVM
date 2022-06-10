
def minimum(a):
    if len(a) == 1:
        return a[0]

    if a[0] < a[1]:
        a.remove(a[1])
        return minimum(a)

    else:
        a.remove(a[0])
        return minimum(a)
