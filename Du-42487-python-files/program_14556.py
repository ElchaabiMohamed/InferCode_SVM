def swap_unique_keys_values(d):
	wards = {}
	bad = {}
	end = {}
	#([('a', 4), ('b', 7), ('c', 10), ('d', 7)])
	for k,v in list(d.items()):
		if v in wards:
			del wards[v]
		elif v not in wards:
			wards[k] = v


	return {v:k for k,v in list(wards.items())}
