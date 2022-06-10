def swap_unique_keys_values(s):
	new_dict = {}
	for key, value in list(s.items()):
		if s[key] not in new_dict:
			new_dict[value] = key
	return new_dict