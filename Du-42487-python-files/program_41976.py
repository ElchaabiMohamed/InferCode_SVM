def swap_unique_keys_values(d):
	d = {}
	d2 = {}
	ds = sorted(list(d.items()), reverse = True)
	for k,v in ds:
		if v not in d:
			d[v] = k
		else:
			d[v] = "N"

	ds2 = sorted(list(d.items()), reverse = True)
	for k,v in ds2:
		if v != "N":
			d2[k] = v
	return d2