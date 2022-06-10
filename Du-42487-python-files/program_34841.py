def swap_unique_keys_values(d):
	nd = {}
	for key in d:
		if d[key] not in nd:
			nd[d[key]] = key
		else:
			del nd[d[key]]
	return nd