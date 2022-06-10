#!/usr/bin/env python

def swap_unique_keys_values(my_dict):
	seen = []
	unseen = []
	for key in list(my_dict.keys()):
		value = my_dict[key]
		if value in seen:
			unseen.append(value)
		else:
			seen.append(value)
	new_dict = {k:v for k, v in list(my_dict.items()) if v not in unseen}
	new_dict = {y:x for x, y in list(new_dict.items())}
	return new_dict