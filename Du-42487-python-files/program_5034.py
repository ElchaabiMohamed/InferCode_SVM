

def sumup(n):
	if n == 0:
		return 0
	total = 0
	for i in range(0, n):
		total + i
	return sumup(n-1) + n
