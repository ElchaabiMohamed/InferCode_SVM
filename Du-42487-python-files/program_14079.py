def maximum(a):
	if len(a) <= 1:
		return a[0]
	return max(a[0], maximum(a[1:]))