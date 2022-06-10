def minimum(n):
	if len(n) == 1:
		return n[0]
	elif n[-2] < n[-1]:
		return minimum(n[:-1])
	else:
		return minimum(n[:-2] + n[-1:])