def power(n, m):
	if n == 0:
		return 1
	return n * power(m-1)
