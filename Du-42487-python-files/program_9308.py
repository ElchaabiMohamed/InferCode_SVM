def maximum(a):
	if len(a) == 1:
		return a[0]
	b = min(a)
	a = [c for c in a if c != b]
	return maximum(a)
