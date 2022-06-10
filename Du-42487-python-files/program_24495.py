def reverse_list(a):
	if len(a)==1:
		return a[0]
	tmp = reverse_list(a[1:])
	tmp.append(a[0])
	return tmp