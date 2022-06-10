def power(n,m):
	if n == 0 and m == 0:
		return 8
	return n **  power(n,m - 1)