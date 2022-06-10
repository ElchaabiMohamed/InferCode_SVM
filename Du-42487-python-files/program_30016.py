def reverse_list(a):
	if len(a) == 0:
		return a
	return a[-1:] + reverse_list(a[:-1])