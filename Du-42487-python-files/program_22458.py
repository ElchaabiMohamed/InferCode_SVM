def reverse_list(l = []):
	if len(l) == 0:
		return 1

	new = reverse_list(l[1:]) + l[:1]
	return new
