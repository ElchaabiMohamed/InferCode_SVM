def swap_unique_keys_values(d):
	new_dic = {}
	keys2swap = [d[key] for key in d]
	
	for k , v in list(d.items()):
		if keys2swap.count(v) == 1:
			new_dic[v] = k
	
	return new_dic