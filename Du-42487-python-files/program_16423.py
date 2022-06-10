def power(n,p):
	if n == 0:
		return 0
	return n**power(n,p-1)