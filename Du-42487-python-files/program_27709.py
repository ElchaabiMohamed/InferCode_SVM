def minimun(l):
	if len(l) == 1:
		return l[0]
	return a[0] < minimun(l[1:])