def power(m, n):
	if m == 0:
		return 1
	if n == 0:
		return 1
	return m ** power(n)