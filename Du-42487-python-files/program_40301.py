def minimum(a):
	if len(a) == 1:
		return a[0]
	smallest = minimum (a[1:])
	if a[0] < smallest:
		smallest = a[0]
	return smallest