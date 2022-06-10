def power(n , p):
	if p == 0:
		return 1
	return power(n ** p)