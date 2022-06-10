def minimum(l):
	if len(l) == 0:
		return 0
	lowest = 100
	for line in l:
		if line < lowest:
			lowest = line

	return minimum(lowest)