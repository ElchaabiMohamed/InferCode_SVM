def minimum(a):
    if a == []:
        return tmp
    if a.pop() < a[-1]:
        print((a[-1]))
        tmp = a.pop()
    return minimum(a)