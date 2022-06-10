
def maximum(l):
	if len(l) == 1:
		return l[0]
	small = l[0]
	for n in l:
		if n < small:
			small = n
	l.remove(small)
	return maximum(l)