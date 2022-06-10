def swap_keys_values(d):
	new_dict = {}
	for key, value in list(d.items()):
		new_dict[value] = key
	return new_dict