def power(m, n):
	if m == 0:
		return 1
	return n * power(m, n - 1)