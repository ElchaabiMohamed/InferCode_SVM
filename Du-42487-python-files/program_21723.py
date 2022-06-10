def minimum(l):
	lowest = 10000000000
	if l == []:
		return lowest
	if int(l[0]) < lowest:
		lowest = int(l[0])
	return minimum(l[0]).pop
