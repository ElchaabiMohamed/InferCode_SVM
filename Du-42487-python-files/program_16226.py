def reverse_list(l):
	if len(l) == 0:
		rl = list()
		return rl
	rl = reverse_list(l[1:])
	rl.append(l[0])
	return rl