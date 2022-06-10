def fibonacci(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n - 1 + fibonacci(n - 1)