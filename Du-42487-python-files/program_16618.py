def swap_keys_values(d):
	for k, v in list(d.items()):
		del d[k]
		d[v] = k