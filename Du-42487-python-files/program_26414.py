def swap_unique_keys_values(d):
	seen = list(d.keys())
	swapped_dict = dict(list(zip(list(d.values()), list(d.keys()))))
	for v, k in swapped_dict:
		if k in seen:
			break
	return swapped_dict