def reverse_list(a):
	if len(a) == 0:
		return []
	return reverse_list(a).append(a[0])