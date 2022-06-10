def reverse_list(l):
	if len(l)==0:
		return []
	elif len(l)==1:
		return l[0]
	else:
		return reverse_list(l[1:]).append(l[0])