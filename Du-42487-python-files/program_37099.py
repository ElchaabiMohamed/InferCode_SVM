def maximum(l):
	try:
		if l[0] > l[1]:
			return maximum(l[:1] + l[2:])
		else:
			return maximum(l[1:])
	except IndexError:
		return l[0]