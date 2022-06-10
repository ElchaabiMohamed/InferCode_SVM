def minimum(a, tmp = 0):
    if a == []:
        return tmp
    if tmp == 0 or a[-1] < tmp:
        tmp = a[-1]      
    return minimum(a[:-1], tmp)