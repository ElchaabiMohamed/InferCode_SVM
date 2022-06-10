import sys

def swap_unique_keys_values(d):
	new_d = {}
	for (k, v) in list(d.items()):
		if v not in new_d:
			new_d[v] = k
	return new_d