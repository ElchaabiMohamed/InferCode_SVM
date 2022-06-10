def fibonacci(a):
	if a == 0 or a == 1:
		return 1
	else:
		return a + fibonacci(a - 1)