import sys

def swap_keys_values(d):
	new_d = {}
	for k, v in list(d.items()):
		new_d[v] = k
	return new_d
