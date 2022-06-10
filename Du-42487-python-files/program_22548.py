def power(n, p):
	if p == 0:
		return 1
	elif p == 1:
		return n
	return n ** (p-1)