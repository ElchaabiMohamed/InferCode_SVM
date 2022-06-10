def minimum(a, tmp = 0):
    if a == []:
        return tmp
    if a[-1] < tmp:
        tmp = a[-1]      
    return minimum(a[:-1], tmp)