def maximum(a, tmp = 0):
    if a == []:
        return tmp
    if tmp == 0 or a[-1] > tmp:
        tmp = a[-1]      
    return maximum(a[:-1], tmp)