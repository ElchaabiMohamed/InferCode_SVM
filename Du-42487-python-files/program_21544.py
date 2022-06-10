def reverse_list(n):
	if len(n) == 0:
		return []
	return [l[-1]] + reverse_list(l[:-1])