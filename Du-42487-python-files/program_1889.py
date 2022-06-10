def reverse_list(a):
	if len(a)==2:
		return("")
	return reverse_list(a[1:]+a[0])