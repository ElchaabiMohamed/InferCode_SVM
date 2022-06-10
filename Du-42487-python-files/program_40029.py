def maximum(a):
	if len(a)==1:
		return a[0]
	biggest = maximum(a[1:])

	if a[0] > biggest:
		return a[0]
	else:
		return biggest  



