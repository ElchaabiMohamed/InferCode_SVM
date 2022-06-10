def maximum(a):
	if len(a) == 1:
		return a[0]

	if a[-2] > a[-1]:
		return maximum(a[:-1])
	else:
		return maximum(a[:-2] + a[-1:])