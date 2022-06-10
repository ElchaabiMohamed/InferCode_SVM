def swap_unique_keys_values(d):
	swapped_dict = {v:k for k,v in list(d.items())}
	return swapped_dict