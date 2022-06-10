def power(n):
	if n == 0:
		return 0
	else: 
		return n ** power(n-1)	