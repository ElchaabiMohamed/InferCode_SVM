def swap_unique_keys_values(d):
	dic={}
	for (key, value) in list(d.items()):
		if value not in dic:
			dic[value]=key
		else: del dic[value]
	return dic
