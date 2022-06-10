import sys 


def swap_keys_values(d):
	dictionary = {}
	for key in d:
		dictionary[d[key]] = key
	return dictionary
