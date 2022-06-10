def fibonacci(n):
	i = 0
	prev = 0
	curr = 1
	while i < n:
		total = curr + prev 
		prev = curr
		curr = total 
		i += 1
	return curr


