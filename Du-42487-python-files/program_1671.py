def minimum(l):
	if len(l) == 1:
		return l[0]
	tmp = minimum(l[1:])
	return tmp if tmp > l[0] else l[0]