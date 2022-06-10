def minimum(n):
	if len(n) == 1:
		return n[0]
	h = n[0]
	t = n[1:]
	m = minimum(t)
	if h > m:
		return m
	else:
		return h