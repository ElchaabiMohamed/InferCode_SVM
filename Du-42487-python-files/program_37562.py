def swap_keys_values(dictionary_descriptor):
	new_dictionary = {}
	for keys,values in dictionary_descriptor:
		new_dictionary[values] = keys