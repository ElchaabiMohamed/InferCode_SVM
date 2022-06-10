import sys

def swap_keys_values(d):
	new_dict = {}
	for (k,v) in list(d.items()):
		if v not in list(new_dict.values()):
			new_dict[v] = k
	return new_dict