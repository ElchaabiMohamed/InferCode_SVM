

def reverse_list(a):
	if a:
		return [a[-1]] + reverse_list(a[:-1])
	else:
		return []