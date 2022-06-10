import sys

def swap_keys_values(d):
	for key in d:
		d[key] = key
	return d
