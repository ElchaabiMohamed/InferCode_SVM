def sumup(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	sumup = sumup(n-1)
	return n + sumup