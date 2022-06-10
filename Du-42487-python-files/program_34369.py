def factorial(n):
	if n == 0:
		return 1

	fact_of_n = factorial(n - 1)
	return n * (n-1)
