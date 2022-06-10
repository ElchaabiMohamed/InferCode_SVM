def minimum(n):
	if len(n) == 1:
		return (n[0])
	else:
		minimum_ret = minimum(n[1:])
		return n[0] if n[0] < minimum_ret else minimum_ret
