def maximum(l):
	max = 0
	if len(l) == 1:
		return l[0]
	else:
		if l[0] > l[1]:
			return maximum(l).pop(l[1])
		else:
			return maximum(l).pop(l[0])