def reverse_list(l):
	if len(l) != 0:
		temp = l.pop(0)
		reverse_list(l)
		l.append(temp)
	return l