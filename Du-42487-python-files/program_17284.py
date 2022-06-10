def minimum(a):
    tmp = a[0]
    for i in a:
        if i > tmp:
            tmp = i
    return tmp