def reverse_list(a):
	if len(a) == 1 or len(a) == 0:
		return a
	can = reverse_list(a[1:])
	can.append(a[0])
	return can