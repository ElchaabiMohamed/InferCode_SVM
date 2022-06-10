def minimum(a):
    if a == []:
        return 1
    tmp = a.pop()
    if tmp < minimun(a):       
        return tmp