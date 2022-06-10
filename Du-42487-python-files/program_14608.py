def minimum(l):
	l = sorted(l)
	if l[0] < l[1]:
		return l[0]

	return minimum(l)