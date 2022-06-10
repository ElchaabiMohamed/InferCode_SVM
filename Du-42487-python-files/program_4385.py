def reverse_list(l):
	if len(l) == 0:
		return []
	a = l[1]
	return reverse_list(l[1:]).append(a)