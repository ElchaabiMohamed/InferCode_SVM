def power(m, n):
	if m == 0:
		return 0
	elif m == 1:
		return 1
	elif n == 0:
		return 1
	elif n == 1:
		return m
	else:
		m * power(m, n-1)
	