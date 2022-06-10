def reverse_list(l):
	if len(l)==2:
		return ' '.join(l[1],l[0]).split(' ')
	else:
		return (''.join(reverse_list(l[1]),l[0]).split())