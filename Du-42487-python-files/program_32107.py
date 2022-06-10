def swap_unique_keys_values(d):
	d2 = {}
	d3 = {}
	ds = sorted(list(d.items()), reverse = True)
	for k,v in ds:
		if v not in d2:
			d2[k] = v
		else:
			d2[v] = "N"
	d2 = sorted(list(d2.items()), reverse = True)
	for k,v in ds2:
		if v != "N":
			d3[k] = v
	return d3