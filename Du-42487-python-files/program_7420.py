def minimum(l):
	lowest = l[0]
	for line in l:
		if line < lowest:
			lowest = line
	return lowest
