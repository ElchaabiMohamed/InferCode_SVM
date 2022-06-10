def reverse_list(a):
	if len(a) == 1 or len(a) == 0:
		return a
	return reverse_list(a[1:]).append(a[0])
