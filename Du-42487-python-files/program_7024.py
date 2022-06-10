def swap_keys_values(dic):
	keys = list(dic.keys())
	values = list(dic.values())
	d = {}
	i = 0
	for v in values:
		d[v[i]] = keys[i]
		i = i + 1