def sumup(n):
	if n==0:
		return n
	return n*sumup(n-1)