def minimum(a):
	if len(a) == 1:
		return a[0]
	h = a[0]
	t = a[1:]
	m = minimum(t)
	if h > m:
		return m
	else:
		return h