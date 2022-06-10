def factorial(n):
	if n * n == 1:
		return 1 
	if n * n == 0:
		return 1

	return n * factorial(n - 1)