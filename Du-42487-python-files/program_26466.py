def reverse_list(l):
	if len(l)==2:
		return list(''.join(l[1],l[0]))
	else:
		return list(''.join(reverse_list(l[1:]),l[0]))