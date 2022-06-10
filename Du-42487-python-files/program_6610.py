

def reverse_list(l):
	if len(l) < 2:
		return l
	else:
		return reverse_list(l[1:]) + l[0]

