def minimum(l):
	a = l[0]
	if len(l)==2:
		if l[1] >= l[0]:
			return l[0]
		else:
			return l[1]
	if a >= minimum(l[:-1]):
		return minimum(l[:-1])

		