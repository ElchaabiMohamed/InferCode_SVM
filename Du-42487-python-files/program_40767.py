def swap_unique_keys_values(s):
	new_dict = {}
	for key, value in list(s.items()):
		if s.count(s[key]) == 1:
			new_dict[value] = key
	return new_dict