n = 0

def minimum(l):
	if len(l) == 1:
		return l[0]

	if l[0] >= minimum(l[1:]):
		return l[0]

	else:
		return minimum(l[(n + 1):])