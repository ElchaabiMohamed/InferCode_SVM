def swap_keys_values(d):
	a = {}
	for k, v in list(d.items()):
		a[v] = k
	return a