def minimum(a):
	if len(a)==1:
		return a[0]
	biggest = minimum(a[1:])

	if a[0] > biggest:
		return a[0]
	else:
		return biggest  



