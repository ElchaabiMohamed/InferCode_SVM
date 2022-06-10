def swap_keys_values(dic):
	keys = list(dic.keys())
	values = list(dic.values())
	d = {}
	i = 0
	for v in values:
		d[keys[i]] = v[i]
		i = i + 1

	return d