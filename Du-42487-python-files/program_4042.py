def minimum(l):
	lowest = l[0]
	if l == []:
		return 0
	if l[0] < lowest:
		lowest = l[0]
	return minimum(l).pop(l[0])