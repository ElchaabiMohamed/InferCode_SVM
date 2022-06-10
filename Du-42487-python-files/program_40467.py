def fibonacci(n):
	if n == 1 or n == 0:
		return 1
	else:
		return n + fibonacci(n - 1)