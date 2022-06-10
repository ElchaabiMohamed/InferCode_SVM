import sys

def swap_keys_values(x):
	for key, v in list(x.items()):
		d[v] = key
	return d

