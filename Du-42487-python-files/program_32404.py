def minimum(n):
	if n == 1:
		return n[0]
	
	else:
		min_ret = minimum
		return n[0] if n[0] < min_ret else min_ret