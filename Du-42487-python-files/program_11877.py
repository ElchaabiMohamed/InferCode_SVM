
def maximum(l):
	if len(l) == 1:
		return l[0]
	f , m = l[0], maximum(l)
	if f > m:
		return f
	else:
		return m