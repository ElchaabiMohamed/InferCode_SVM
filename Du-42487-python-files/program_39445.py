def reverse_list(l):
	if len(l)==2:
		a = []
		a.append(l[1])
		a.append(l[0])
		return a
	return reverse_list(l[1:]).append(l[0])