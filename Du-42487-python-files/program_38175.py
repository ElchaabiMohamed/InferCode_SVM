def swap_unique_keys_values(dictionary_descriptor):
	new_dictionary = {}
	addthese = set()
	for keys,values in list(dictionary_descriptor.items()):
		if values in new_dictionary:
			addthese.update([values])
			del new_dictionary[values]
		elif values not in new_dictionary:
			new_dictionary[values] = keys 


	return(new_dictionary)