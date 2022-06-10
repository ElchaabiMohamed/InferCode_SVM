def swap_keys_values(d):
	dic={}
	for (key, value) in list(d.items()):
		dic[value]=key
	return dic
