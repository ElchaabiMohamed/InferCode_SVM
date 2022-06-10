def swap_unique_keys_values(d):
	seen = list(d.keys())
	swapped_dict = dict(list(zip(list(d.values()), list(d.keys()))))
	
	print((list(swapped_dict.values())))
	return swapped_dict