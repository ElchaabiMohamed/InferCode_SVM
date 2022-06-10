def reverse_list(l):
	if len(l)==0:
		return []
	else:
		return [l[-1]].append(reverse_list(l[:-1]))