def minimum(n):
	if n == 0:
		return n
	
	elif n[0] < minimum(n[1::]):
		return n[0]
	
	else: 
		n[0] > n[1::]
	return minimum(n - 1)