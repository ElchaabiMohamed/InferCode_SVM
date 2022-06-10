def maximum(n):
	if len(n) == 1:
		return n[0]
	elif n[-2] > n[-1]:
		return maximum(n[:-1])
	else:
		return maximum(n[:-2] + n[-1:])