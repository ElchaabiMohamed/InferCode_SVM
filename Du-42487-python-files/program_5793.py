def minimum(s):
	if len(s) == 1:
		return 0
	else:
		max = maxElement(L[1:])
		if L[0] > max:
			return L[0]
		else:
			return max