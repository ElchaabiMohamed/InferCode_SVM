def reverse_list(l = []):
	if len(l) == 0:
		return l

	new = reverse_list(l[1:]) + l[:1]
	return new
