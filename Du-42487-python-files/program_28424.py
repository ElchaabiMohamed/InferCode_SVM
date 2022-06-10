def reverse_list(l):
	x = []
	i = len(l) - 1
	while i != -1:
		x.append(l[i])
		i -= 1
	return x