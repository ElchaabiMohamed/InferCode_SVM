def swap_unique_keys_values(dic):
	keys = list(dic.keys())
	values = list(dic.values())
	d = {}
	values = []
	keys = []
	for v in list(dic.values()):
		values.append(v)
	for k in list(dic.keys()):
		keys.append(k)
	i = 0 
	while i < len(values):
		if values[i] not in d:
			d[values[i]] = keys[i]
		elif values[i] in d:
			del d[values[i]]
		i = i + 1
	return d