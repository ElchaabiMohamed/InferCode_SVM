def minimum(a, flag = True):
    if a == []:
        return tmp
    if flag == True:
        tmp = a.pop()
    if a[-1] < tmp:
        tmp =a[-1]      
    return minimum(a[:-1], flag = False)