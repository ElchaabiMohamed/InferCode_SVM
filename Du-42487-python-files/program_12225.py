def minimum(l):
	if len(l) == 1:
		return l[0]
	else:
		mini = minimum(l[1:])
		if l[0] < mini:
			return l[0]
		else:
			return mini
			
