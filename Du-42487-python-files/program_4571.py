

def reverse_list(a):
	return [a[-1]] + reverse_list(a[:-1]) if a else []