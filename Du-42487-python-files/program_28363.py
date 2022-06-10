def power(m, n):
	if n == 1:
		return m
	if n == 0:
		return 1

	return n * power(m, n-1)