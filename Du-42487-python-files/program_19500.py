def fibonacci(nth):
		if nth == 1 or nth == 0:
			return 1
		return (nth + 1) + fibonacci(nth - 1)