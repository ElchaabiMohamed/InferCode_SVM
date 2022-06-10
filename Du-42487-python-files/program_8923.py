def swap_keys_values(s):
	new_dict = {}
	for key, value in list(s.items()):
		new_dict[value] = key
	return new_dictict