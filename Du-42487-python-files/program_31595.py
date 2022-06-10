def swap_keys_values(d):
	newd = {}
	for key in d:
		newd[d[key]] = key

	return newd