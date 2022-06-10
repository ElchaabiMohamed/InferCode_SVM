def fibonacci(i):
	if i<= 1:
		return 1
	else:
		return (fibonacci(i-1) + fibonacci(i-2))
