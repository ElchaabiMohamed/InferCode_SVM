def maximum(k):
	if len(k) == 1:
		return k[0]
	if k[0] > maximum(k[1:]):
		return k[0]

	else:
		return maximum(k[1:])
