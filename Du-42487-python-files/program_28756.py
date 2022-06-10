#!/usr/bin/env python

def swap_unique_keys_values(my_dict):
	seen = []
	unseen = []
	for key in list(my_dict.keys()):
		value = my_dict[key]
		if value in unseen:
			seen.append(value)
		else:
			unseen.append(value)
	new_dict = {v:k for k, v in list(my_dict.items()) if v not in seen}
	return new_dict
	
my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
print((swap_unique_keys_values(my_dict)))