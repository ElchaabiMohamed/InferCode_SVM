def minimum(n):
	if n == 1:
		return n[0]
	
	else:
		return n[0] if n[0] < minimum else minimum