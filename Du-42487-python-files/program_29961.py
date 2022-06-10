def minimum(l):
	lowest = 10000000000
	print((l[0]))
	if l == []:
		return lowest
	if l[0] < lowest:
		lowest = l[0]
	return minimum(l[0]).pop
