def fibonacci(l):
	if l == 0 or l == 1:
		return 1

	return fibonacci(l-1) + fibonacci(l-2)