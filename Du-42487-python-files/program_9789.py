def reverse_list(a):
	if len(a) == 0:
		return []
	return reverse_list(a[1:]).append(a[0])