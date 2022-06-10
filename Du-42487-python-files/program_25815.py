

def reverse_list(a):
	if not a:
		return a
	else:
		return reverse_list(a[1:] + a[0])