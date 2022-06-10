def swap_unique_keys_values(dictionary_descriptor):
	new_dictionary = {}
	addthese = set()
	for keys,values in list(dictionary_descriptor.items()):
		addthese.update(values , keys)
		new_dictionary[addthese[values]] = addthese[keys]


	return(new_dictionary)