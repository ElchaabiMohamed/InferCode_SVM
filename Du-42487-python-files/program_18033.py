def reverse_list(a):
	if a==[]:
		return a
	tmp = reverse_list(a[1:])
	tmp.append(a[0])
	return tmp