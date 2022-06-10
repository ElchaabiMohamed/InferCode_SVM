def maximum(l):
	if len(l) == 1:
		return l[0]
	else:
		m = maximum(l[1:])
		if l[0] > m:
			return l[0]
		else:
			return m
			
