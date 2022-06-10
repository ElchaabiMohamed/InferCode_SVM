import sys

def swap_unique_keys_values(d):
	nd = {}
	to_delete = []

	for k,v in list(d.items()):
		if v in nd:
			to_delete.append(v)
		else:
			nd[v] = k

	for k in to_delete:
		del nd[k]

	return nd