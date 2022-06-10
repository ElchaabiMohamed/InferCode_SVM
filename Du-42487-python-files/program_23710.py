def reverse_list(l):
	if len(l) == 0:
		return l[0]

	return l.append(reverse_list(l[:1]))
