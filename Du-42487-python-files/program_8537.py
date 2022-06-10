def maximum(n):
	if len(n) == 1:
		return n[0]
	h = n[0]
	t = n[1:]
	m = maximum(t)
	if m > h:
		return m
	else:
		return h