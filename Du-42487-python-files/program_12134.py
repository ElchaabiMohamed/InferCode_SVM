def minimum(a):
	if len(a) == 1:
		return a[0]
	a.remove(max(a))
	return minimum(a)