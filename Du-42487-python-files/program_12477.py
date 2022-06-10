def maximum(l):
	if len(l) == 1:
		return l[0]
	m = maximum(l[1:])
	return m if m > l[0] else l[0]