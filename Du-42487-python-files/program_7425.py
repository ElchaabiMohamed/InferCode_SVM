def power(n,m):
	if n == 0 and m == 0:
		return 1
	return n **  power(n,m - 1)