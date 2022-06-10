def factorial(n):
	if n == 0:
		return 0
	return n + n * factorial(n-1)