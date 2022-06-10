def reverse_list(a):
	if len(a)==1:
		return a[0]
	b = []
	b.append(reverse_list(a))
	return b[-1::]