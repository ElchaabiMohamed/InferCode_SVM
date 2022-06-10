def factorial(n):
	if n == 1:
		return 1


	factorial_of_n = factorial(n - 1)
	return n * factorial_of_n
