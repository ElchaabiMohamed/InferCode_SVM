def minimum(a):
    if a.pop() < a[-1]:
        tmp = a.pop()
    if a == []:
        return tmp
    return minimum(a)