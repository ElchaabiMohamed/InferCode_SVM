def minimum(a):
	if len(a) == 1:
		return a
	else:
		if a[0] < a[1]:
			del a[1]
		else:
			del a[0]
		return minimum(a)