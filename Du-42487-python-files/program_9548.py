def swap_unique_keys_values(d): #s = dictionary d
	new_d = {}
	unique = set()
	for k,v in list(d.items()):
		if v in new_d:
			unique.update([v])
			del new_d[v]
		else:
			new_d[v] = k

	return new_d
