def maximum(l):
	l = sorted(l)
	if l[len(l) - 1] > l[len(l) - 2]:
		return l[len(l) - 1]

	return maximum(l)