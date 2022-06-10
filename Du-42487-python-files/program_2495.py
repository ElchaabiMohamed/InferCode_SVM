def minimum(n):
	if len(n) == 1:
		return n
	if n[0] > minimum(n[1::]):
		return n + 1
	else:
		return minimum(n - 1) 