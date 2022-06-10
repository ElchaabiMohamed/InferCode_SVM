def swap_keys_values(dic):
	d = []
	for key in dic:
		value = dic[key]
		d[value] = key
	return d