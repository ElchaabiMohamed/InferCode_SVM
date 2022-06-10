def reverse_list(a, x = []):
	if len(a) == 1:
		return a
	f = reverse_list[:-1]
	x.append(f)
	return x
