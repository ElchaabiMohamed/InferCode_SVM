def sumup(n):
	if n == 0:
		return 0
	sumup = sumup(n-1)
	return n + sumup