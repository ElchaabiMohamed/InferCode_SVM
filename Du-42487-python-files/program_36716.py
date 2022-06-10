def swap_keys_values(dictionary_descriptor):
	new_dictionary = {}
	for keys,values in list(dictionary_descriptor.items()):
		new_dictionary[values] = keys