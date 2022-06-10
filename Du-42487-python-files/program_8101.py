import sys

def swap_unique_keys_values(d):
	nd = {}
	for k, v in list(d.items()):
		if not v in nd:
			nd[v] = k
		else:
			del nd[v]

	return nd

