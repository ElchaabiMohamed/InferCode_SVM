def swap_keys_values(d):
	new_dict = {}
	old = sorted(d.items())
	for pair in old:
		if pair[1] not in new_dict:
			new_dict[pair[1]] = pair[0]
	return new_dict