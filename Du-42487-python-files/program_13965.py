def fibonacci(nth):
		if nth == 1 or nth == 0:
			return 1
		return fibonacci(nth - 1) + fibonacci(nth - 2)