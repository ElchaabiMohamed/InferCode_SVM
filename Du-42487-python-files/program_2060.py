def power(m, n):
	if n == 0:
		return m
	m *= n
	return power(m, n-1)