#!/usr/bin/env python

def swap_keys_values(my_dict):
	new_dict = {y:x for x,y in list(my_dict.items())}
	return new_dict