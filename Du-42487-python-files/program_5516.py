def swap_unique_keys_values(dic):
	new_dic = {}
	add = set()
	for keys,values in list(dic.items()):
		if values in new_dic:
			add.update([values])
			del new_dic[values]
		elif values not in new_dic:
			new_dic[values] = keys 


	return(new_dic)