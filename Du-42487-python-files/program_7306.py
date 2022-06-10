def reverse_list(l):
	if len(l) == 1:
		return l[0]

	else:
		return (l[::1], reverse_list(l[::1]))