def swap_unique_keys_values(d):

	new_d = {}

	for key,value in list(d.items()):
		
		if value not in list(d.values()):

			new_d[value] = key

	return new_d