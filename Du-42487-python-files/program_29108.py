def minimum(l):
	if len(l)==1:
		return l[0]
	if minimum(l[:-1]) >= minimum(l[1:]):
		return minimum(l[1:])
	else:
		return minimum(l[:-1])

		