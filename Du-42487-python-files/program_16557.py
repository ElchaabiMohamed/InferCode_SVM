def sumup(n):
	if n == 0:
		return 0
	n = n + sumup(n-1)
