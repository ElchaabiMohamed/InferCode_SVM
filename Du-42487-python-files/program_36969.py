def maximum(a):
	if len(a) == 1:
		return a[0]
	else:
		if a[0] > a[1]:
			del a[1]
		else:
			del a[0]
		return maximum(a)