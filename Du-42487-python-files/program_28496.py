def reverse_list(a):
	if len(a) == 1:
		return a
	b = a[1:]
	return (reverse_list(b)).append(a[0])