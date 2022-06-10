def minimum(a):
	if len(a) == 1:
		return a[0]

	if a[-2] < a[-1]:
		return minimum(a[:-1])
	else:
		return minimum(a[:-2] + a[-1:])