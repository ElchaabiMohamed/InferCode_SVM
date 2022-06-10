def minimum(l):
	if len(l) == 1:
		return l[0]

	mini = minimum(l[1])
	if l[0] < mini:
		l.pop(mini)
	else:
		l.pop(l[0])
	return l[0]
