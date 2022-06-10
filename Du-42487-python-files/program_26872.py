import sys

def swap_key_values(d):
	new_dict = {}
	for k, v in list(d.keys()), list(d.values()):
		new_dict[v] = k

	return new_dict