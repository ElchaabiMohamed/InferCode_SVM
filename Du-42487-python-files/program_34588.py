def minimum(l):
	a = l[len(l)-1]
	if len(l)==1:
		return l[0]
	if a >= minimum(l[:-1]):
		return minimum(l[-1])

		