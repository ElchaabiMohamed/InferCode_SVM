def power(n, p):
	if p == 0:
		return 1
	po = power(p-1)
	return po * n