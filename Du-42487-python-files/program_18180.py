import sys

def swap_keys_values(d):
	nd = {}

	for k,v in list(d.items()):
		nd[v] = k

	return nd