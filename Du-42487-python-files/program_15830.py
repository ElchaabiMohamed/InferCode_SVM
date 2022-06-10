def power(n, x):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return n * power(x-1)
