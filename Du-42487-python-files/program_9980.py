import sys

def swap_unique_keys_values(d):
	d2 = {}
	for key in d:
		if d[key] in d2:
			del d2[d[key]]
		else:
			d2[d[key]] = key
	return d2
