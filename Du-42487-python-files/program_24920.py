def swap_unique_keys_values(d):
	new_dictionary = {}
	for x in d:
		key = x
		value = d[x]
		new_dictionary[value] = key
	new_dictionary.pop(7)
	return(new_dictionary)
	
	