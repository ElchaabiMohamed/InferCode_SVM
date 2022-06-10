import sys

def swap_keys_and_values(d):
	d = {}

	for k,v in list(d.items()):
		d[v] = k

	return d