def power(m, n):
	if m == 0:
		return 1
	return m * power(m, n - 1)