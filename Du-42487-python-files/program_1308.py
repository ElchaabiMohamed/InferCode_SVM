def power(m, n):
	if n == 0:
		return 8
	return n * power(n, m - 1)