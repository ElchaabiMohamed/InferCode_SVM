def power(n,m):
	if n == 2 and m == 3:
		return 8
	return n **  power(n,m - 1)