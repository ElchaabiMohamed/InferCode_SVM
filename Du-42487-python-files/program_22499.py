def swap_unique_keys_values(dictionary_descriptor):
	new_dictionary = {}
	for keys,values in list(dictionary_descriptor.items()):
		try: 
			new_dictionary[values] = keys
		except KeyError:
			pass

	return(new_dictionary)