def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	n -= 1
	x = fibonacci(n) + fibonacci(n-1)
	return x