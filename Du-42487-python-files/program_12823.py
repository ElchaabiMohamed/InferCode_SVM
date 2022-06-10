def swap_unique_keys_values(dic):
	new = {}
	new = {val:key for (key,val) in list(dic.items())}
	return(new)