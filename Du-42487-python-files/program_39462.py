def minimum(a):
	if len(a) == 1:
		return a
	b = max(a)
	a.replace(b, '')
	return minimum(a)
