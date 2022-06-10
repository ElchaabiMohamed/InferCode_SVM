def fibonacci(a):
	x = a
	if a == 0 or a == 1:
		return 1
	
	else:
		return a + fibonacci(a - x)