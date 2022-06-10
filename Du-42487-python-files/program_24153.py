import sys

def swap_keys_values(x):
	d = dict((v,k) for k,v in list(x.items()))
	return x