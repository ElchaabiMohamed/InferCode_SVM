

def minimum(l):
	if len(l) == 1:
		return l
	f, m = l[0], minimum(l[1:])
	if f < m:
		return f
	else:
		return m



