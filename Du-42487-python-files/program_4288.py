import sys

def swap_unique_keys_values(d_0):
	d = {}
	for key in d_0:
		if d_0[key] not in d:
			d[d_0[key]] = key
		else:
			del d[d_0[key]]

	return d