def minimum(k):
	if len(k) == 1:
		return k[0]
	if k[0] < minimum(k[1:]):
		return k[0]

	else:
		return minimum(k[1:])
