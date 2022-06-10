def power(a,b):
	if a**b == 0:
		return 1

	return power(a**b)