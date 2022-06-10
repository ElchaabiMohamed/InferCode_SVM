def minimum(l):
	min = 10000000000
	for x in l:
		if x < min:
			min = x
	return min