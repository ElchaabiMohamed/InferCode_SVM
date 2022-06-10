def power(m, n):
	if n == 0:
		return m
	m *= m
	return power(m, n-1)