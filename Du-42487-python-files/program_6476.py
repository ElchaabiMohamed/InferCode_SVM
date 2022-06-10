def reverse_list(a): # [1, 2, 3] 
	if len(a) == 0:
		return []
	return reverse_list(a[1:]) + [a[0]]