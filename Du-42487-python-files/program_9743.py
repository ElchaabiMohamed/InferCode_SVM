def swap_unique_keys_values(d):
	wards = {}
	#([('a', 4), ('b', 7), ('c', 10), ('d', 7)])
	for k,v in list(d.items()):
		if v in wards:
			bad[k] = v
		else:
			wards[k] = v


	return {v:k for k,v in list(d.items())}