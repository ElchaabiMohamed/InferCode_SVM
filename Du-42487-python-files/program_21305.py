

def maximum(l, currmax = None):
	if not l:
		return currmax
	pos = l.pop()

	if currmax == None or pos > currmax:
		return maximum(l, pos)
	return maximum(l, currmax)