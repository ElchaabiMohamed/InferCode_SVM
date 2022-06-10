def reverse_list(l=[]):
	i = 0
	new_list = []
	while i < len(l):
		new_list.append(l[len(l)-i])
		i += 1

	return new_list