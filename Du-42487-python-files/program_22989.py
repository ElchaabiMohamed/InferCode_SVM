def fibonacci(nth):
		if nth == 1 or nth == 0:
			return 1
		return (nth - 1) + power(nth - 2)