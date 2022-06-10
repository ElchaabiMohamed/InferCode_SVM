import sys

def swap_keys_values(d):
	keys = list(d.keys())
	values = list(d.values())
	new_dict = {}
	for i in range(len(keys)):
		if values.count(values[i]) == 1:
			new_dict[values[i]] = keys[i]
	return new_dict