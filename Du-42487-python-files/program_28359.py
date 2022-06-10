def minimum(l):
	if len(l) == 1:
		return l[0]

	minimum = minimum(l[1])
	if l[0] < minimum:
		l.pop(minimum)
	else:
		l.pop(l[0])
	return l[0]
