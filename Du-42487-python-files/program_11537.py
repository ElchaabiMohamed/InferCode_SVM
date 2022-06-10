#!/usr/bin/env python3

def swap_unique_keys_values(d):
	new_dict = {}
	for k, v in list(d.items()):
		if v not in new_dict:
			new_dict = k
		else:
			del new_dict[v]
	return new_dict
