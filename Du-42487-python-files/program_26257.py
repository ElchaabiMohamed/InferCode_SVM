def swap_unique_keys_values(d):
	dic = {}
	for key in d:
		value = d[key]
		dic[value] = key
	new_dic = {}
	for key in dic:
		new_dic[key] = dic[key]
	return new_dic