def swap_unique_keys_values(d):
	new_d = {}
	for k, v in list(d.items()):
		if d[k] in new_d:
			del new_d[k]
		else:
			new_d[v] = k
	return new_d