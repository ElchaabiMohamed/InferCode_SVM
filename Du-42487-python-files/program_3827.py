import sys

def swap_keys_values(x):
	d = dict((k,v) for v,k in list(x.items()))
	return x

