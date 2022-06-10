def swap_unique_keys_values(d):
	swapped_dict = dict(list(zip(list(d.values()), list(d.keys()))))
	return set(swapped_dict)