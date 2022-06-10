def reverse_list(a):
	if len(a)==0:
		return(a)
	return [l[-1]]+reverse_list(l[:-1])

	return reverse_list(a[a:])