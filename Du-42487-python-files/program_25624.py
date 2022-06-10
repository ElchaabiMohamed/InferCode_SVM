def power(n, p):
	if n == 0:
		return 1
	return n * power(n, p-1)	