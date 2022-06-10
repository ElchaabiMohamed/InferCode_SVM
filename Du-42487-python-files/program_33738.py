

def reverse_list(a):
	if a == '':
		return a

	else:
		return reverse_list(a[1:] + a[0])