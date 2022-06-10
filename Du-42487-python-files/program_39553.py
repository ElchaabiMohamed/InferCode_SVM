def reverse_list(a, b = 0):
	if a == 0:
		return 0
	c = reverse_list[-1::]
	a.append(c)
	return c