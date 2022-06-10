def swap_keys_values(dic):
	keys = list(dic.keys())
	values = list(dic.values())
	d = {}
	values = []
	keys = []
	for v in list(dic.values()):
		values.append(str(v))
	for k in list(dic.keys()):
		keys.append(k)
	i = 0 
	while i < len(values):
		d[values[i]] = keys[i]
		i = i + 1
	return sorted(d)