def power(m, n):
	if n == 0:
		return 1
	elif m == 0:
		return 0

	a = power(m - 1, n - 1)
	return m ** power_of_n