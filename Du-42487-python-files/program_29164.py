def reverse_list(l):
	if len(l) == 0:
		return []
	return [l[-1]] + reverse_list(l[:-1])

	



print((reverse_list([1,2,3])))
