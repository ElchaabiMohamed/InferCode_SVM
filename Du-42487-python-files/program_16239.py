import sys

def swap_keys_values(x):
	d ={}
	for key, v in list(x.items()):
		d[v] = key
	return d

