def swap_keys_values(d): #s = dictionary d
	new_d = {}
	key = sorted(d.keys())
	value = sorted(d.values())

	for i in range(0, len(key)):
		new_d[value[i]] = key[i]

	return new_d

