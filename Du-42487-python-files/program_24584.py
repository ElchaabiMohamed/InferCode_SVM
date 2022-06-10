def swap_keys_values(s): #s = dictionary d
	new_d = {}
	key = sorted(d.keys())
	value = sorted(d.values())

	for i in range(0, len(key) - 1):
		new_d[key[i]] = value[i]

	return new_d

