def reverse_list(a):
	if len(a)==1:
		return(a)

	return a+reverse_list(a[1:1])