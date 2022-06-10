def reverse_list(lst):
	if lst == []:
		return []
	return lst[-1] + reverse_list(lst[:-1])