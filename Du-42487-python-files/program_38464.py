def minimum(l):
	if len(l) == 1:
		return l[0]
	elif a[0] < minimum(l[1:]):
		return a[0]
	return minimum(l[1:])