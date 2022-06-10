def minimum(a):
    m = a[0]
    for n in a:
        if m > n:
            m = n
    return(m)  
