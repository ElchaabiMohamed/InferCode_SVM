def minimum(l):
	if len(l) == 1:
		return l[0]
	else:
		new_l = minimum(l[1:])
	if l[0] < new_l:
		return l[0]
	else:
		return new_l