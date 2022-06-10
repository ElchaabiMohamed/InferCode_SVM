def minimum(l):
	if len(l) == 1:
		return l[0]
	elif l[0] > minimum(l[1:]):
		return l[0]
	return minimum(l[1:])