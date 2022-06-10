import sys

def swap_unique_keys_values(d):
	new_d = {}
	seen = []
	for v in list(d.values()):
		if v not in seen:
			seen.append(v)
		elif v in seen:
			seen.remove(v)
	
	for (k,v) in list(d.items()):
		if v in seen:
			new_d[v] = k
	return new_d