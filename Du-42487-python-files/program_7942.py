def swap_keys_values(d):
	dic = {}
	for key in d:
		value = d[key]
		dic[value] = key
	new_dic = {}
	for key in dic:
		if key not in new_dic:
			new_dic[key] = key
	return new_dic