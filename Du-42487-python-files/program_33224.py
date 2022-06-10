def maximum(l):
	if len(l) == 1:
		return l[0]
	max = maximum(l[1:])
	if l[0] > max:
		return l[0]
	else:
		return max