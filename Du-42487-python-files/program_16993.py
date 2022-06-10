def swap_unique_keys_values(d):
	values = list(d.values())
	unique = [x for x in values if values.count(x) == 1]
	swapped_dict = 0

	if unique in values:
		swapped_dict = dict(list(zip(list(d.values()), list(d.keys()))))
	return swapped_dict