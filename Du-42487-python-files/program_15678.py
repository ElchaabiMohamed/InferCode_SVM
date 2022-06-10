
def minimum(l):
	if len(l) == 1:
		return l[0]
	large = l[0]
	for num in l:
		if num > large:
			large = num
	return l.remove(large)