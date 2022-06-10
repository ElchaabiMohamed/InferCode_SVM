def reverse_list(a):
	if len(a)==1:
		return a[0]
	b = []
	i=0
	b.append(reverse_list(a[i])) + 1
	return b[-1::]