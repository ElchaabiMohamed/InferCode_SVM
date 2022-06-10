
def swap_keys_values(d):
	new_d = {}
	for keys in d:
		new_d[d[keys]] = keys
	return new_d