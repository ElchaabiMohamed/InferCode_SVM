def swap_keys_values(d):
	new_dic = {}
	for k , v in list(d.items()):
		new_dic[v] = k
	
	return new_dic