def power(m, n):
	if n == 0:
		return 0
	return n * power(n, m - 1)