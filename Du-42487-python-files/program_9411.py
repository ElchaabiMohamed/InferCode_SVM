def reverse_list(l):
	return reverse_list(l[1:-1]).append(l[0])