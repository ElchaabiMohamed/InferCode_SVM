def maximum(a):
	if len(a) == 1:
		return a[0]
	a.remove(min(a))
	return maximum(a)