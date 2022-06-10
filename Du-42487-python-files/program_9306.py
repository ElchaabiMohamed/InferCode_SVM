import sys

def swap_keys_values(d):
	new_dict = {}
	keys = list(d.keys())
	values = list(d.values())
	for i in range(len(keys)):
		if values.count(values[i]) == 1:
			new_dict[values[i]] = keys[i]
	return new_dict