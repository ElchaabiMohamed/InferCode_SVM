def reverse_list(a):
	if len(a) == 0 or len(a) == 1:
		return 1
	else:
		return [a[-1]] + reverse_list(a[:-1])