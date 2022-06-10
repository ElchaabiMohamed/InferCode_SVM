def reverse_list(l):
	if len(l)==2:
		return l[1].append(l[0])
	return reverse_list(l[1:]).append(l[0])