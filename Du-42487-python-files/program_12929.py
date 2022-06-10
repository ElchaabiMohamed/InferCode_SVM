
def minimum(l):

	if len(l) == 1:
		return l[0]

	smallest = minimum(l[1:])

	if l[0] < smallest:
		return l[0]
	else:
		return smallest
