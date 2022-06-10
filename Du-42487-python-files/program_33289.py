def reverse_list(l):
	if not l:
		return l
	return reverse_list(l[1:]) + [l[0]]