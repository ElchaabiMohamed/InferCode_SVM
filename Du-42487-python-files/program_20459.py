import sys

def swap_keys_values(d):
	d2 = {}
	for key in d:
		d2[d[key]] = key
	return d2
