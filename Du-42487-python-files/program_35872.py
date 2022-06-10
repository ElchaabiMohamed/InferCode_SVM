import sys

def swap_keys_values(d_0):
	d = {}
	for key in d_0:
		d[d_0[key]] = key

	return d