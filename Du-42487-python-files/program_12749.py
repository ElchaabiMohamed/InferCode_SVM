def minimun(l):
	if len(l) == 1:
		return l[0]
	elif a[0] < minimun(l[1:]):
		return a[0]
	return a[0] < minimun(l[1:])