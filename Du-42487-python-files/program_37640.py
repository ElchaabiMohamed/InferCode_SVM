def swap_unique_keys_values(d):
	d1 = {}
	new_dict = {}
	for k,v in d:
		if d[v] not in d1 :
			d1[v] = k
		else:
			d1[v] = ''
	for k,v in d1:
		if v != '':
			new_dict[k] = v
		
	return new_dict