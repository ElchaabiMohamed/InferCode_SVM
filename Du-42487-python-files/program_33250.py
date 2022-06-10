def minimum(l):
	if len(l) == 1:
		return l[0]

	if l[-2] < l[-1]:
		return minimum(l[:-1])
	else:
		return minimum(l[:-2] + l[-1:])