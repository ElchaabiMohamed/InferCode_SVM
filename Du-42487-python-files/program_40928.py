def factorial(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0

	sum_to_n_1 = factorial(n - 1)
	return n * sum_to_n_1
