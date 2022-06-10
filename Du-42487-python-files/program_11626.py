def minimum(l):
	if len(l) == 1:
		return l[0]

	if a[-2] < a[-1]:
		return minimum(a[:-1])
	else:
		return minimum(a[:-2] + a[-1:])