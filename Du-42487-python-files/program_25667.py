def reverse_list(l):
	if len(l) == 1:
		return l

	return reverse_list(l[-1::])