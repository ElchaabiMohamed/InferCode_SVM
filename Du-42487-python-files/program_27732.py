def power(m, n):
	if n == 0:
		return m
	m = m ** 2
	return power(m, n-1)