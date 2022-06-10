

def minimum(l, currmin = None):
	if not l:
		return currmin
	pos = l.pop()

	if currmin == None or pos < currmin:
		return minimum(l, pos)
	return minimum(l, currmin)