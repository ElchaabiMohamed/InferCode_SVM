def reverse_list(l):
	if not l:
		return []
	else:
		return reverse_list(l[1:]).append(l[0])
		
