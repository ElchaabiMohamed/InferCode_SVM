def maximum(a):
	if len(a) == 1:
		return list(a[0])
	return maximum(a.remove(min(a)))