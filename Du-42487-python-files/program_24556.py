def minimum(a):
	if len(a) == 1:
		return a[0]
	return minimum(a.remove(max(a)))