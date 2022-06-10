def minimum(a):
	if len(a) == 1:
		return a[0]
	b = max(a)
	a = [c for c in a if c != b]
	return minimum(a)
