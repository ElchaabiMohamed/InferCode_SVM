def power(m, n):
	if n == 0:
		return 1
	elif m == 0:
		return 0

	b = power(n - 1)
	return m ** b