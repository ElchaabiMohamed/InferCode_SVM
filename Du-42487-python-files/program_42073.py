def power(m, n):
	if n == 0:
		return 1
	return m + m * power(m, n-1)