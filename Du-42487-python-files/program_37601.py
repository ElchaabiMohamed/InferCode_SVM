#!/usr/bin/env python3
import sys

def swap_unique_keys_values(my_dict):
	unique_dict = {}
	for k,v in list(my_dict.items()):
		if v in unique_dict:
			del unique_dict[v]
		else:
			unique_dict[v] = k

	return unique_dict
