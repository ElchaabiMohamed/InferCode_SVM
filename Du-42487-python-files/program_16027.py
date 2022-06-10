def reverse(l):
	if len(l) == 1:
		return l

	return reverse(l[:-1] + l[0])