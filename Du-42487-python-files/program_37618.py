def swap_unique_keys_values(d):
	new_dic = {}
	for k , v in list(d.items()):
		if d[k] not in new_dic:
			new_dic[v] = k
	
	return new_dic