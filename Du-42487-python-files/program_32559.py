def fibonacci(n):
	if n <= 1:
		return 1
	return n + fibonacci(n - 1) + fibonacci(n - 2)