def maximum(a):
	if len(a) == 1:
		return a[0]
	h = a[0]
	t = a[1:]
	m = maximum(t)
	if m > h:
		return m
	else:
		return h