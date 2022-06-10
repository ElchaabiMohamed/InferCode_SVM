def reverse_list(l):
	if len(l)==0:
		return []
	return reverse_list(l).append(l[0])