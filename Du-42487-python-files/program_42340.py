def reverse_list(l):
	return lambda l: (backwards (l[1:]) + l[:1] if l else [])
