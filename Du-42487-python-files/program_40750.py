def maximum(l):

	if len(l) == 1:
		return l[0]

	biggest = maximum(l[1:])

	if l[0] > biggest:
		return l[0]
	else:
		return biggest