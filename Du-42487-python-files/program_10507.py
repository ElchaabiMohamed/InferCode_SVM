def maximum(l):
	if len(l)==1:
		return l[0]
	if maximum(l[:-1]) >= maximum(l[1:]):
		return maximum(l[:-1])
	else:
		return maximum(l[1:])