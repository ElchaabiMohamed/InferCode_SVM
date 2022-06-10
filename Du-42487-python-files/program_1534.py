def minimum(l):
	a = l[0]
	if len(l)==1:
		return l[0]
	elif a >= minimum(l):
		return minimum(l[:-1])

		