
def maximum(a):
    if len(a) == 1:
        return a[0]
    else:
    	l = maximum(a[1:])
    if a[0] < l:
    	return a[0]
    else:
    	return l