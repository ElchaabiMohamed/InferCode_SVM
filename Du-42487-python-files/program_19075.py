def fibonacci(h):
	if h == 0 or h == 1:
		return(1)
	return(fibonacci(h-1) + fibonacci(h-2))