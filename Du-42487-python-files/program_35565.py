def swap_unique_keys_values(d):
	new_dict = {}
	for k in d:
		v = d.has(k)
		if v in new_dict:
			del new_dict[v]
		else:
			new_dict[v] = k
			
	return new_dict