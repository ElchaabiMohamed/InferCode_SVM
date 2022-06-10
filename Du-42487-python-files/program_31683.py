def swap_unique_keys_values(d):
	values = list(d.values())
	unique = [x for x in values if values.count(x) == 1]
	swapped_dict = 0

	if unique in values:
		swapped_dict = {v:k for k,v in list(d.items())}
	return swapped_dict