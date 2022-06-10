import sys

def swap_unique_keys_values(d):
	new_d = {}
	for k, v in list(d.items()):
		if v not in list(new_d.keys()):
			new_d[v] = k
		else:
			new_d.pop(v)
	return new_d
