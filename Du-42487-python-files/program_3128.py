def minimum(l):
	if len(l) == 1:
		return l[0]
	mini = minimum(l[1:])
	if l[0] > mini:
		return mini
	else:
		return l[0]