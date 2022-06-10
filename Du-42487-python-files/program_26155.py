def power(m, n):
	if n == 1:
		return m
	m = m ** 2
	return power(m, n-1)