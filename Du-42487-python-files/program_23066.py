def power(m,n):
	if m == 0:
		return m
	return m + power(m, n - 1)