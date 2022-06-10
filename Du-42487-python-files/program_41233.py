def reverse_list(l):
	if len(l) == 0:
		return []

	a = l[-1]
	a.pop()
	return [a] + reverse_list(l)