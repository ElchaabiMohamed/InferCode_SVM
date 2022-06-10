def swap_unique_keys_values(d):
	d2 = {}
	d3 = {}
	ds = sorted(list(d.items()), reverse = True)
	for k,v in ds:
		if v in d2:
			d2[v] = "N"
		else:
			d2[v] = k
	ds2 = sorted(list(d2.items()), reverse = True)
	for k,v in ds2:
		if v != "N":
			d3[k] = v
	return d3