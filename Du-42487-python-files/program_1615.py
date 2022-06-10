
#!/usr/bin/env python3
import sys

def swap_keys_values(my_dict):
	swapped_dict = {}
	dict_items = sorted(my_dict.items())
	for i in dict_items:
		key , value = i[0] , i[1]
		swapped_dict[value] = key

	return swapped_dict