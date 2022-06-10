def minimum(l):
	if l == []:
		return []
	lowest = 100
	for line in l:
		if line < lowest:
			lowest = line

	return minimum(lowest)