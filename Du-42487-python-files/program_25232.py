def fibonacci(l):
	if l == 1 or l == 0:
		return 1
	l -= 1
	return fibonacci(l) + fibonacci(l-1)
print((fibonacci(7)))