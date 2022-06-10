def fibonacci(n):
	if n == 0:
		return 1
	elif n < 3:
		return n
	return fibonacci(n-2) + fibonacci(n-1)