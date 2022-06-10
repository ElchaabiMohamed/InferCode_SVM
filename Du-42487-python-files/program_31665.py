import sys

def swap_unique_keys_values(d):
	new_dict = {}
	for k, v in list(d.items()):
		if v not in new_dict:
			new_dict[v] = k

	return new_dict