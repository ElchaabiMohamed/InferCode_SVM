def maximum(l):
	if len(l) == 1:
		return l[0]
	maxi = maximum(l[1:])
	if l[0] < maxi:
		return maxi
	else:
		return l[0]