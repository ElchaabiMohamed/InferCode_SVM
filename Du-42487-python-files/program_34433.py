def reverse_list(l):
	if len(l) == reverse_list(l):
		return l
	return 1 + reverse_list(l[-1]+ l[:-1])