def swap_keys_values(d): #s = dictionary d
	new_d = {}
	for k,v in list(d.items()):
		new_d[v] = k

	return new_d
