def swap_keys_values(original_dict):
	swapped_dict = {}
	for key in original_dict:
		swapped_dict[original_dict[key]]= key
	return swapped_dict