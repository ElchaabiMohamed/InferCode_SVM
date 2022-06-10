import sys

def swap_keys_values(x):
	d = {v: k for k, v in list(x.items())}
	return d