def sumup(n):
	if n == 1:
		return 1
	sumup = sumup(n-1)
	return n + sumup