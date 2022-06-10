def minimum(l):
	if len(l)==1:
		return l[0]
	else:
		for i in l:
			if i >= minimum(l[1:]):
				return minimum(l[1:])

		