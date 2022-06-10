
def minimum(a):
    if len(a) == 1:
        return n[0]
    else:
    	l = minimum(l[1:])
    if a[0] < l:
    	return l[0]
    else:
    	return l