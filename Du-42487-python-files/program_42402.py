
def minimum(a):
    if len(a) == 1:
        return a[0]
    else:
    	l = minimum(a[1:])
    if a[0] < l:
    	return l[0]
    else:
    	return l