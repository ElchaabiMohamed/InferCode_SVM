def fibonacci(i, n = 1):
	if i == 1 or i == 0:
		return 1
	return fibonacci(i - 1) + fibonacci(i - 2)