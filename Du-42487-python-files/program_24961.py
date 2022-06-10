

def minimum(a):
	if len(a) == 1:
		return a[0]
	small = a[0]
	if a[1] < small:
		small = a[1]
	else:
		a.remove(a[0])
	return minimum(a)