def minimum(l):
	min = sum(l)
	for i in l:
		if i < min:
			min = i
	return min