

def minimum(a):
	if len(a) == 1:
		return a[0]
	small = a[0]
	i = 0
	if a[i+1] < small:
		small = a[i]
	else:
		a.remove(a[i])
	return minimum(a)