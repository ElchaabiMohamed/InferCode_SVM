def minimum(n):
	if len(n) == 1:
		print((n[0]))
	if l[0] < minimum(l[1:]):
		return l[0]
	else:
		return minimum(l[1:])