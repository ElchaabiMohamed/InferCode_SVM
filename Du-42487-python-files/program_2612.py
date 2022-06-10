def minimum(l):
	if len(l) == 1:
		return l[0]
	else:
		if minimum(l[0:len(l)]) < minimum(l[len(l)+1:]):
			return minimum(l[0:len(l)])
		else:
			return minimum(l[len(l)+1:])
			
