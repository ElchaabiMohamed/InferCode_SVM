def power(m, n):
	if n == 0:
		return 1
	elif m == 0:
		return 0

	power_of_n = power(n - 1)
	return m ** power_of_n