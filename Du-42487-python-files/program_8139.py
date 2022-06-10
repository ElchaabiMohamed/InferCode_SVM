def swap_keys_values(d):
	new_dictionary = {}
	for x in d:
		key = x
		value = d[x]
		new_dictionary[value] = key
	return(new_dictionary)
	
	